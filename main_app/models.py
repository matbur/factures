from operator import mul

from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy


class Contractor(models.Model):
    name = models.CharField(max_length=50)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    NIP = models.CharField(max_length=10, unique=True)

    def save(self, *args, **kwargs):
        if not self.validate_nip(self.NIP):
            raise ValidationError(
                ugettext_lazy('NIP: %(nip) is incorrect'),
                params={'nip': self.NIP}
            )
        super().save(*args, **kwargs)

    @staticmethod
    def validate_nip(nip):
        nip = nip.replace('-', '')
        if len(nip) != 10 or not nip.isdigit():
            return False
        *digits, crc = map(int, nip)
        weights = (6, 5, 7, 2, 3, 4, 5, 6, 7)
        check_sum = sum(map(mul, digits, weights))
        return check_sum % 11 == crc

    def __str__(self):
        return '{}, NIP:{}'.format(self.name, self.NIP)


class Invoice(models.Model):
    date = models.DateField(default=timezone.now)
    number = models.PositiveIntegerField()
    issuer = models.ForeignKey(Contractor, related_name='issuer')
    receiver = models.ForeignKey(Contractor, related_name='receiver')

    def __str__(self):
        return '#{} on {} from {} to {}'.format(
            self.number, self.date, self.issuer, self.receiver
        )


class Line(models.Model):
    invoice = models.ForeignKey(Invoice)
    description = models.CharField(max_length=100)
    price = models.FloatField()
    amount = models.PositiveSmallIntegerField(default=1)
    tax = models.PositiveSmallIntegerField(default=23)

    class Meta:
        unique_together = ['invoice', 'description']

    def calculate_net(self):
        return round(self.price * self.amount, 2)

    def calculate_gross(self):
        return round(self.calculate_net() * (1 + self.tax / 100), 2)

    def __str__(self):
        return '{}: ({} + {}%) * {}'.format(
            self.description, self.price, self.tax, self.amount
        )


def get_net(self):
    l = Line.objects.filter(invoice=self)
    s = sum(i.calculate_net() for i in l)
    return round(s, 2)


def get_gross(self):
    l = Line.objects.filter(invoice=self)
    s = sum(i.calculate_gross() for i in l)
    return round(s, 2)


Invoice.get_net = get_net
Invoice.get_gross = get_gross
