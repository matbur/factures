from rest_framework.serializers import HyperlinkedModelSerializer

from .models import Contractor, Invoice, Line


class ContractorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Contractor
        fields = ('name', 'address1', 'address2', 'NIP')


class LineSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Line
        fields = ('invoice', 'description', 'price', 'amount', 'tax', 'net', 'gross')


class InvoiceSerializer(HyperlinkedModelSerializer):
    # lines = LineSerializer(many=True, read_only=True)
    # issuer = ContractorSerializer()
    # receiver = ContractorSerializer()

    class Meta:
        model = Invoice
        fields = ('date', 'number', 'issuer', 'receiver', 'lines', 'total_net', 'total_gross')
