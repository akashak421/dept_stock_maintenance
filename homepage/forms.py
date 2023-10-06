from django import forms
from .models import Chairs, Tables

class ChairForm(forms.ModelForm):
    class Meta:
        model = Chairs
        fields = ['lab_name', 'categories1', 'categories2', 'categories3', 'status']

    lab_name = forms.ChoiceField(choices=Chairs.LAB_CHOICES, required=True)
    categories1 = forms.ChoiceField(choices=Chairs.CATEGORY1_CHOICES, required=True)
    categories2 = forms.ChoiceField(choices=Chairs.CATEGORY2_CHOICES, required=True)
    categories3 = forms.ChoiceField(choices=Chairs.CATEGORY3_CHOICES, required=True)
    status = forms.ChoiceField(choices=Chairs.STATUS_CHOICES, required=True)

class TableForm(forms.ModelForm):
    class Meta:
        model = Tables
        fields = ['lab_name', 'categories1', 'categories2', 'status']

    lab_name = forms.ChoiceField(choices=Tables.LAB_CHOICES, required=True)
    categories1 = forms.ChoiceField(choices=Tables.CATEGORY1_CHOICES, required=True)
    categories2 = forms.ChoiceField(choices=Tables.CATEGORY2_CHOICES, required=True)
    status = forms.ChoiceField(choices=Tables.STATUS_CHOICES, required=True)
