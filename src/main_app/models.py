from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from .validators import validate_nip


class Contractor(models.Model):
    name = models.CharField(max_length=50)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    NIP = models.CharField(max_length=10, unique=True)

    def save(self, *args, **kwargs):
        if not validate_nip(self.NIP):
            raise ValidationError(f'NIP: {self.NIP} is incorrect')
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}({self.NIP})'


class Line(models.Model):
    invoice = models.ForeignKey('Invoice', related_name='lines')
    description = models.CharField(max_length=100)
    price = models.FloatField()
    amount = models.PositiveSmallIntegerField(default=1)
    tax = models.PositiveSmallIntegerField(default=23)

    class Meta:
        unique_together = ['invoice', 'description']

    @property
    def net(self):
        n = self.price * self.amount
        return round(n, 2)

    @property
    def gross(self):
        g = self.net * (1 + self.tax / 100)
        return round(g, 2)

    def __str__(self):
        return f'{self.description}: ({self.price} + {self.tax}%) * {self.amount}'


class Invoice(models.Model):
    def get_next_number(self=None):
        num = Invoice.objects.filter(
            date__month=timezone.now().month,
            date__year=timezone.now().year
        ).count()
        return num + 1

    date = models.DateField(default=timezone.now)
    number = models.PositiveIntegerField(default=get_next_number)
    issuer = models.ForeignKey(Contractor, related_name='issuer')
    receiver = models.ForeignKey(Contractor, related_name='receiver')

    def save(self, *args, **kwargs):
        if self.issuer == self.receiver:
            raise ValidationError('Issuer and receiver cannot be the same')
        super().save(*args, **kwargs)

    def lines(self):
        l = Line.objects.filter(invoice=self)
        return l

    @property
    def total_net(self):
        l = Line.objects.filter(invoice=self)
        s = sum(i.net for i in l)
        return round(s, 2)

    @property
    def total_gross(self):
        l = Line.objects.filter(invoice=self)
        s = sum(i.gross for i in l)
        return round(s, 2)

    def __str__(self):
        return f'#{self.number} on {self.date} from {self.issuer} to {self.receiver}'
