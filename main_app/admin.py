from django.contrib import admin

from .models import Contractor, Invoice, Line

# Register your models here.
admin.site.register(Contractor)


# admin.site.register(Invoice)
# admin.site.register(Line)
class LineInline(admin.TabularInline):
    model = Line
    extra = 2


class InvoiceAdmin(admin.ModelAdmin):
    inlines = [LineInline]
    list_display = ['date', 'number', 'issuer', 'receiver']
    list_display_links = ['number']


admin.site.register(Invoice, InvoiceAdmin)
