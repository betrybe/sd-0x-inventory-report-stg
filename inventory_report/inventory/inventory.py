from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xml.etree.ElementTree as ET


class Inventory:
    @classmethod
    def generate_report(cls, file, request_type):
        if request_type == "simples":
            return SimpleReport.generate(file)
        if request_type == "completo":
            return CompleteReport.generate(file)

    @classmethod
    def csv_importer(cls, file, request_type):
        all_products = []
        with open(file) as products:
            csv_products = csv.DictReader(
                products, delimiter=",", quotechar='"'
            )
            for row in csv_products:
                all_products.append(dict(row))
        return cls.generate_report(all_products, request_type)

    @classmethod
    def json_importer(cls, file, request_type):
        all_products = []
        with open(file) as products:
            json_products = json.load(products)
            for prod in json_products:
                all_products.append(prod)
        return cls.generate_report(all_products, request_type)

    @classmethod
    def xml_importer(cls, file, request_type):
        root = ET.parse(file).getroot()
        all_products = []
        for record in root.findall("record"):
            product = {}
            for child in list(record):
                product[child.tag] = child.text.strip()
            all_products.append(product)
        return cls.generate_report(all_products, request_type)

    @classmethod
    def import_data(cls, file, request_type):
        if file.endswith(".csv"):
            return cls.csv_importer(file, request_type)
        if file.endswith(".json"):
            return cls.json_importer(file, request_type)
        if file.endswith(".xml"):
            return cls.xml_importer(file, request_type)
