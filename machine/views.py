from django.shortcuts import render
from django.http import HttpResponse
from django.core.files import File
from dateutil.parser import parse

import csv

from machine.models import MachineModel, Supplier, Machine, Ledger
from company.models import Country, County, Site, Company

class OldAddress(object):
    id = None
    desc = None
    street_1 = None
    street_2 = None
    town = None
    county = None
    post_code = None
    country = None
    contact = None
    telephone = None

    def map(self, row):
        self.id = row["ID"]
        self.desc = self.__format(row["Desc"])
        self.street_1 = self.__format(row["Street1"])
        self.street_2 = self.__format(row["Street2"])
        self.town = self.__format(row["Town"])
        self.post_code = self.__format(row["PostCode"])
        self.contact = self.__format(row["Contact"])
        self.telephone = self.__format(row["Telephone"])

        if self.__format(row["County"]) is None:
            self.county = None
        else:
            # See if an existing County exists which matches the name
            try:
                self.county = County.objects.get(name=row["County"])
            except County.DoesNotExist:
                self.county = County()
                self.county.name = row["County"]
                self.county.save()

        if self.__format(row["Country"]) is None:
            self.country = None
        else:
            # See if an existing Country exists which matches the name
            try:
                self.country = Country.objects.get(name=row["Country"])
            except Country.DoesNotExist:
                self.country = Country()
                self.country.name = row["Country"]
                self.country.save()

    # Format a value to exclude empty values
    def __format(self, value):
        if value is None or value == "" or value == "NULL":
            return None
        else:
            return value

class Import(object):
    path = "/Users/Adam/Development/python/ojfreshmachinedb/data/"

    # Addresses. Old ID -> Old Address Object
    addresses = dict()

    # Machine Model. Old ID -> MachineModel Object
    models = dict()

    # Suppliers. Old Name -> New Supplier Object
    suppliers = dict()

    machines = dict()

    def run_all(self):

        Machine.objects.all().delete()

        self.run_address_pre_load()
        self.run_machine_model_import()
        self.run_machine_import()
        self.run_ledger_import()
        pass

    # Load machine models
    def run_machine_model_import(self):
        with open(self.path + "models.csv", 'rU') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Try and locate an existing row with the same name
                try:
                    model = MachineModel.objects.get(name=row['Name'])
                except MachineModel.DoesNotExist:
                    model = MachineModel()
                    model.name = row["Name"]
                    model.save()

                self.models[row["ID"]] = model

    # Load all addresses and pre-map some values
    def run_address_pre_load(self):
        with open(self.path + "address.csv", 'rU') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                address = OldAddress()
                address.map(row)

                self.addresses[row["ID"]] = address

    def run_machine_import(self):
        with open(self.path + "machines.csv", 'rU') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:

                # Load the supplier mappings
                if self.__has_value(row["Supplier Name"]) == False:
                    supplier = None
                else:
                    try:
                        supplier = Supplier.objects.get(name=row['Supplier Name'])
                    except Supplier.DoesNotExist:
                        supplier = Supplier()
                        supplier.name = row["Supplier Name"]
                        supplier.save()

                self.map_to_machine(row)

    def map_to_machine(self,row):
        ojstore = Site.objects.get(address_1="IN STORE",company__name="OJ Fresh")
        supplier = self.suppliers.get(row["Supplier Name"])

        m = Machine()
        m.bought_date = self.__format_date(row["Bought Date"])
        m.bought_exchange_rate = self.__format_decimal(row["Exchange Rate"])
        m.bought_price = self.__format_decimal(row["Bought Price"])
        m.invoice_date = self.__format_date(row["Invoice Date"])
        m.is_fixed_asset = self.__format_bool(row["Fixed Asset"])
        #m.last_maintenance = self.__format_date(row["Last Maintenance"])
        m.last_pat = self.__format_date(row["Last PAT Test"])
        m.machine_model = self.models.get(row["Model ID"])
        m.manufacture_date = self.__format_date(row["Manufacture Date"])
        m.next_maintenance = self.__format_date(row["Next Maintenance"])
        m.next_pat = self.__format_date(row["Next PAT Test"])
        m.on_loan = self.__format_bool(row["On Loan"])
        m.serial = self.__format(row["Serial Number"])
        m.site = ojstore
        m.sold_exchange_rate = self.__format_decimal(row["Exchange Rate"])
        m.sold_price = self.__format_decimal(row["Sold Price"])
        m.supplier = supplier
        m.supplier_invoice = self.__format(row["Supplier Invoice Number"])

        m.save()
        self.machines[row["Machine ID"]] = m

    def run_ledger_import(self):
        with open(self.path + "ledger.csv", 'rU') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                #ID,Date,Type,Details,MachineID
                l = Ledger()
                l.date = self.__format_date(row["Date"])
                l.machine = self.machines.get(row["MachineID"])
                l.comment = row["Details"]
                l.type = l.COMMENT if row["Type"] == "Comment" else l.MAINTENANCE

                l.save()

    def __format_decimal(self,value):
        return value if value != "NULL" else None

    def __format_date(self, value):
        return parse(value) if value != "NULL" else None

    def __format_bool(self, value):
        return True if value == "1" or value == "True" else False

    def __has_value(self,value):
        return False if value is None or value == "" or value == "NULL" else True

    # Format a value to exclude empty values
    def __format(self, value):
        if value is None or value == "" or value == "NULL":
            return ""
        else:
            return value

class ImportNew(object):
    path = "/Users/Adam/Development/python/ojfreshmachinedb/data/"

    def run_all(self):
        with open(self.path + "new_machines.csv", 'rU') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                #Company,Site,Manufacter,Model,Serial

                # Try to find a company
                try:
                    company = Company.objects.get(name=row['Company'])
                except Company.DoesNotExist:
                    company = Company()
                    company.name = row["Company"]
                    company.save()

                # Try to find a site in the company with the same name
                try:
                    site = Site.objects.get(address_1=row['Site'],company=company)
                except Site.DoesNotExist:
                    site = Site()
                    site.address_1 = row["Site"]
                    site.company = company
                    site.save()

                # Try to find a matching model
                try:
                    model = MachineModel.objects.get(name=row["Manufacter"] + " " + row["Model"])
                except MachineModel.DoesNotExist:
                    model = MachineModel()
                    model.name = row["Manufacter"] + " " + row["Model"]
                    model.save()

                machine = Machine()
                machine.site = site
                machine.machine_model = model
                machine.serial = row["Serial"]
                machine.save()

def index(request):
    i = ImportNew()
    i.run_all()

    return HttpResponse()