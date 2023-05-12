from django import forms
from .models import Part, ProductType, PartType, Material, Jewelry


# Form for part
class PartForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = ["name", "volume", "category", "ModelFile", "status"]
        labels = {
            "name": "Наименование детали",
            "volume": "Объем детали",
            "category": "Категория детали",
            "ModelFile": "Файл модели",
            "status": "Статус детали",
        }
        widgets = {
            "ModelFile": forms.ClearableFileInput(attrs={"multiple": False}),
            "status": forms.Select(choices=[(0, "Inactive"), (1, "Active")]),
        }
        # Add the following line to set the encoding type
        enctype = "multipart/form-data"


# Form class for product type
class ProductTypeForm(forms.ModelForm):
    class Meta:
        model = ProductType
        fields = ["name", "volumeCoefficient", "status"]
        labels = {
            "name": "Наименование",
            "volumeCoefficient": "Коэфициент объема",
            "status": "Статус",
        }


# Django form for partType class
class PartTypeForm(forms.ModelForm):
    class Meta:
        model = PartType
        fields = ["name", "productType"]


# Django form for material class
class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ["name", "price", "density", "materialJSON"]


# Django form for jewelry class
class JewelryForm(forms.ModelForm):
    class Meta:
        model = Jewelry
        fields = [
            "name",
            "parts",
            "ispublic",
            "type",
            "material",
            "user",
            "preview",
            "update_time",
            "status",
            "weight",
            "cost",
            "is_editable",
        ]
