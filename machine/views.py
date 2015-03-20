from django.http import HttpResponse

import csv

from machine.models import MachineModel, Machine
from company.models import Site, Company

class ImportNew(object):
    path = "https://aprice30.github.io/ojfreshmachinedb/data/"

    def run_all(self):
        with open("new_machines.csv", 'rU') as csvfile:
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