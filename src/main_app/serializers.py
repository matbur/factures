from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Contractor, Invoice, Line


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class ContractorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contractor
        fields = ('name', 'address1', 'address2', 'NIP')


class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Line
        fields = ('description', 'price', 'amount', 'tax', 'net', 'gross')


class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    lines = LineSerializer(many=True)
    issuer = ContractorSerializer()
    receiver = ContractorSerializer()

    class Meta:
        model = Invoice
        fields = ('url', 'date', 'number', 'issuer', 'receiver', 'lines')
