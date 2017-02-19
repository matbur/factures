from rest_framework import routers
from rest_framework.viewsets import ModelViewSet

from .models import Contractor, Invoice, Line
from .serializers import InvoiceSerializer, ContractorSerializer, LineSerializer


# Create your views here.


class ContractorViewSet(ModelViewSet):
    queryset = Contractor.objects.all()
    serializer_class = ContractorSerializer


class InvoiceViewSet(ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class LineViewSet(ModelViewSet):
    queryset = Line.objects.all()
    serializer_class = LineSerializer


router = routers.DefaultRouter()

router.register(r'contractors', ContractorViewSet)
router.register(r'invoices', InvoiceViewSet)
router.register(r'lines', LineViewSet)
