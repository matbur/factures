from django.db import models
from django.utils import timezone


class Contractor(models.Model):
    name = models.CharField(max_length=50)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    NIP = models.CharField(max_length=50)

    def __str__(self):
        return '{}, NIP:{}'.format(self.name, self.NIP)


class Invoice(models.Model):
    date = models.DateField(default=timezone.now)
    number = models.PositiveIntegerField()
    issuer = models.ForeignKey(Contractor, related_name='issuer')
    receiver = models.ForeignKey(Contractor, related_name='receiver')

    class Meta:
        unique_together = ['issuer', 'receiver']

    def __str__(self):
        return '#{} on {} from {} to {}'.format(
            self.number, self.date, self.issuer, self.receiver
        )


class Line(models.Model):
    invoice = models.ForeignKey(Invoice)
    description = models.TextField()
    price = models.FloatField()
    amount = models.PositiveSmallIntegerField(default=1)
    tax = models.PositiveSmallIntegerField(default=23)

    def __str__(self):
        return '{}: ({} + {}%) * {}'.format(
            self.description, self.price, self.tax, self.amount
        )
