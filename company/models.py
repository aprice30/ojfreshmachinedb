from django.db import models
from machine.models import Machine

class Contact(models.Model):
    TEL = 'TEL'
    MOB = 'MOB'
    FAX = 'FAX'
    CONTACT_TYPE_CHOICES = (
        (TEL, "Telephone"),
        (MOB, "Mobile"),
        (FAX, "Fax")
    )

    name = models.CharField(max_length=200,blank=True)
    number = models.CharField(max_length=200,blank=True)
    type = models.CharField(max_length=3,
                            choices=CONTACT_TYPE_CHOICES,
                            default=TEL)

    def __unicode__(self):
        return "%s [%s:%s]" % (self.name, self.type, self.number)

class County(models.Model):
    name = models.CharField(max_length=200,unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'County'
        verbose_name_plural = 'Counties'
        ordering = ['name']

class Country(models.Model):
    name = models.CharField(max_length=200,unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        ordering = ['name']

class Address(models.Model):
    address_1 = models.CharField(max_length=200,blank=True)
    address_2 = models.CharField(max_length=200,blank=True)
    address_3 = models.CharField(max_length=200,blank=True)
    town = models.CharField(max_length=200,blank=True)
    county = models.ForeignKey(County,null=True,blank=True)
    post_code = models.CharField(max_length=10,blank=True,verbose_name="Post Code")
    country = models.ForeignKey(Country, null=True,blank=True)

    @staticmethod
    def to_string(cls):
        value = ""
        if len(cls.address_1) > 0:
            value += cls.address_1
        if len(cls.town) > 0:
            value += ",%s" % cls.town
        if len(cls.post_code) > 0:
            value += ",%s" % cls.post_code
        return value

    def __unicode__(self):
        address = Address.to_string(self)
        return address if len(address) > 0 else "No Address Given"

    class Meta:
        verbose_name = 'Address'

class Company(Address):
    name = models.CharField(max_length=200,unique=True)

    def __unicode__(self):
        return self.name;

    def total_sites(self):
        return len(Site.objects.filter(company=self))

    def total_machines(self):
        return len(Machine.objects.filter(site__company=self))

    def primary_contact(self):
        # TODO: When we have done validation to ensure there can be Only one Primary change to get
        contacts = CompanyContact.objects.filter(company=self,is_primary=True)

        if len(contacts) > 0:
            return contacts[0]
        return "--"

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        ordering = ['name']

class CompanyContact(Contact):
    company = models.ForeignKey(Company)
    is_primary = models.BooleanField(default=False,verbose_name="Is Primary?")

    class Meta:
        verbose_name = 'Contact'
        ordering = ['-is_primary']

class Site(Address):
    company = models.ForeignKey(Company,
                                help_text="Try to fill out the address as it will make identifying the site easier.")

    def __unicode__(self):
        address = Address.to_string(self)
        if (len(address) > 0):
            return "%s @ %s" % (self.company, address)
        else:
            return "%s" % (self.company)

    def total_machines(self):
        return len(Machine.objects.filter(site=self))

    def primary_contact(self):
        # TODO: When we have done validation to ensure there can be Only one Primary change to get
        contacts = SiteContact.objects.filter(site=self,is_primary=True)
        if len(contacts) > 0:
            return contacts[0]
        return "--"

    def address_to_string(self):
        return self.__unicode__()
    address_to_string.short_description = "Address"

    class Meta:
        verbose_name = 'Site'
        ordering = ['company']

class SiteContact(Contact):
    site = models.ForeignKey(Site)
    is_primary = models.BooleanField(default=False,verbose_name="Is Primary?")

    class Meta:
        verbose_name = 'Contact'
        ordering =['-is_primary']





