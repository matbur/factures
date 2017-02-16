from django.contrib.auth.models import User
from rest_framework import routers, viewsets

from .models import Contractor, Invoice
from .serializers import UserSerializer, InvoiceSerializer, ContractorSerializer


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ContractorViewSet(viewsets.ModelViewSet):
    queryset = Contractor.objects.all()
    serializer_class = ContractorSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'contractors', ContractorViewSet)
router.register(r'invoices', InvoiceViewSet)
