from django.contrib import admin
from company.models import Company, CompanyContact, County, Country
from company.models import Site, SiteContact
from machine.models import Machine

class SiteContactInline(admin.TabularInline):
    model = SiteContact
    extra = 0

class CompanyContactInline(admin.TabularInline):
    model = CompanyContact
    extra = 0

class SiteInline(admin.StackedInline):
    model = Site
    fk_name = 'company'
    extra = 0

class CompanyAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,              {'fields': ['name']}),
        ('Address',         {'fields': ['address_1','address_2','address_3','town','county','post_code','country'],
                             'classes': ['collapse']})
    ]

    list_display = ['name', 'primary_contact','total_sites','total_machines']
    inlines = [CompanyContactInline]
    search_fields = ['name','address_1','post_code']

class MachineInline(admin.StackedInline):
    model = Machine
    extra = 0

    fieldsets = [
        (None,                  {'fields': [('serial','machine_model','manufacture_date')]}),
        (None,                  {'fields': [('on_loan','is_fixed_asset')]}),
        ('PAT Dates',           {'fields': [('last_pat','next_pat')],
                                 'classes': ['collapse']}),
        ('Maintenance Dates',   {'fields': [('last_maintenance','next_maintenance')],
                                 'classes': ['collapse']}),
        ('Purchase Info',       {'fields': [('supplier','supplier_invoice'),('bought_date','bought_price','bought_exchange_rate')],
                                 'classes': ['collapse']}),
        ('Sale Info',           {'fields': [('invoice_number','invoice_date'),('sold_price','sold_exchange_rate')],
                                 'classes': ['collapse']})
    ]


class SiteAdmin(admin.ModelAdmin):

    fieldsets = [
        (None,              {'fields': ['company']}),
        ('Address',         {'fields': ['address_1','address_2','address_3','town','county','post_code','country']})
    ]

    list_display = ('address_to_string','company','primary_contact','total_machines')
    inlines = [SiteContactInline, MachineInline]
    search_fields = ['address_1','post_code','company__name']

admin.site.register(Company, CompanyAdmin)
admin.site.register(County)
admin.site.register(Country)
admin.site.register(Site, SiteAdmin)