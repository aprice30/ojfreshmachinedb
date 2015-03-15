from django.contrib import admin
from machine.models import Machine, Ledger, MachineModel, Supplier

class LedgerInline(admin.TabularInline):
    model = Ledger
    extra = 0

    fields = ['type','date','comment']

class MachineAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['site']}),
        (None,                  {'fields': [('serial','machine_model','manufacture_date')]}),
        ('PAT Dates',           {'fields': [('last_pat','next_pat')]}),
        ('Maintenance Dates',   {'fields': [('last_maintenance','next_maintenance')]}),
        (None,                  {'fields': [('on_loan','is_fixed_asset')]}),
        ('Purchase Info',       {'fields': [('supplier','supplier_invoice','bought_date'),('bought_price','bought_exchange_rate')],
                                 'classes': ['collapse']}),
        ('Sale Info',           {'fields': [('invoice_number','invoice_date'),('sold_price','sold_exchange_rate')],
                                 'classes': ['collapse']})
    ]

    list_display = ['serial','site','machine_model','next_pat','on_loan','is_fixed_asset']
    inlines = [LedgerInline]
    list_filter = ('on_loan','is_fixed_asset','next_pat','next_maintenance')
    search_fields = ['serial','site__company__name','machine_model__name','site__address_1']

# Date
# All, Past, 1 Month, 6 Month

admin.site.register(Machine, MachineAdmin)
admin.site.register(MachineModel)
admin.site.register(Supplier)