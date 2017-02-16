from operator import mul

from django.db import models
from django.utils import timezone


class Contractor(models.Model):
    name = models.CharField(max_length=50)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50)
    NIP = models.CharField(max_length=10)

    def validate_nip(self, nip):
        nip = nip.replace('-', '')
        if len(nip) != 10 or not nip.isdigit():
            return False
        *digits, crc = map(int, nip)
        wages = (6, 5, 7, 2, 3, 4, 5, 6, 7)
        check_sum = sum(map(mul, digits, wages))
        return check_sum % 11 != crc

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

    def __str__(self):
        return '{}: ({} + {}%) * {}'.format(
            self.description, self.price, self.tax, self.amount
        )
