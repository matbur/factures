from django.contrib import admin

from .models import Contractor, Invoice, Line

# Register your models here.
admin.site.register(Contractor)


class LineInline(admin.TabularInline):
    model = Line
    extra = 2


class InvoiceAdmin(admin.ModelAdmin):
    inlines = [LineInline]
    list_display = ['date', 'number', 'issuer', 'receiver', 'total_net', 'total_gross']
    list_display_links = ['number']
    list_filter = ['date']


admin.site.register(Invoice, InvoiceAdmin)
