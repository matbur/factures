from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Contractor, Invoice


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class ContractorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contractor
        fields = '__all__'


class InvoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'
