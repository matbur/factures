from django.contrib import admin

from .models import Contractor, Invoice, Line

# Register your models here.
admin.site.register(Invoice)
admin.site.register(Contractor)
admin.site.register(Line)
