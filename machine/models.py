from django.db import models
from datetime import date

from django.contrib.admin import SimpleListFilter

class FuturePastDateFilter(SimpleListFilter):
    # Human-readable title which will be displayed in the
    # right admin sidebar just above the filter options.
    title = 'Date Filter'

    # Parameter for the filter that will be used in the URL query.
    parameter_name = 'futurepast'

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return (
            ('past', 'In Past'),
            ('1', '1 Month'),
            ('3', '3 Month'),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """

        now = date.today()

        # Compare the requested value (either '80s' or 'other')
        # to decide how to filter the queryset.
        if self.value() == 'past':
            return queryset.filter(birthday__gte=date(1980, 1, 1),
                                    birthday__lte=date(1989, 12, 31))
        if self.value() == '90s':
            return queryset.filter(birthday__gte=date(1990, 1, 1),
                                    birthday__lte=date(1999, 12, 31))

class MachineModel(models.Model):
    name = models.CharField(max_length=200,unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Model'
        ordering = ['name']

class Supplier(models.Model):
    name = models.CharField(max_length=200,unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Supplier'
        ordering = ['name']

class Machine(models.Model):
    site = models.ForeignKey('company.Site')
    serial = models.CharField(max_length=32,blank=True,verbose_name="Serial #",
                              help_text="Try to specify if possible, leave blank if not known.")
    machine_model = models.ForeignKey(MachineModel,verbose_name="Model")
    invoice_number = models.CharField(max_length=32,blank=True,verbose_name="Invoice No.")
    invoice_date = models.DateField(null=True,blank=True,verbose_name="Invoice Date")
    bought_date = models.DateField(null=True,blank=True,verbose_name="Date")
    supplier = models.ForeignKey(Supplier,null=True,blank=True)
    supplier_invoice = models.CharField(max_length=32,blank=True,verbose_name="Supplier Invoice")
    bought_price = models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True,verbose_name="Price")
    bought_exchange_rate = models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True,verbose_name="Exchange Rate")
    sold_price = models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True,verbose_name="Price")
    sold_exchange_rate = models.DecimalField(max_digits=7,decimal_places=2,null=True,blank=True,verbose_name="Exchange Rate")
    manufacture_date = models.DateField(null=True,blank=True,verbose_name="Manufacture Date")
    last_pat = models.DateField(null=True,blank=True,verbose_name="Last PAT")
    next_pat = models.DateField(null=True,blank=True,verbose_name="Next PAT")
    last_maintenance = models.DateField(null=True,blank=True,verbose_name="Last Maintenance")
    next_maintenance = models.DateField(null=True,blank=True,verbose_name="Next Maintenance")
    on_loan = models.BooleanField(default=False,verbose_name="On Loan")
    is_fixed_asset = models.BooleanField(default=False,verbose_name="Is Fixed Asset")

    def __unicode__(self):
        serial = "UNKNOWN" if self.serial == "" else self.serial
        return "#%s [%s]" % (serial,self.machine_model)

    class Meta:
        verbose_name = 'Machine'
        ordering = ['serial']

class Ledger(models.Model):
    COMMENT = "COMMENT"
    MAINTENANCE = "MAINTENANCE"

    LEDGER_CHOICES = (
        (COMMENT, "Comment"),
        (MAINTENANCE, "Maintenance")
    )

    comment = models.TextField()
    date = models.DateField(default=date.today)
    type = models.CharField(max_length=11,
                            choices=LEDGER_CHOICES,
                            default=COMMENT)
    machine = models.ForeignKey(Machine)
    # Photos

    def __unicode__(self):
        # If the comment is longer than 100 then trim it down
        comment = self.comment
        if len(comment) > 100:
            comment = "%s..." % comment[0:100]
        return "%s '%s'" % (self.type, comment)

    class Meta:
        verbose_name = 'Ledger Item'
        ordering = ['-date']