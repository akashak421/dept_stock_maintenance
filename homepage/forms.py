from django import forms
from .models import Chairs, Tables

class ChairForm(forms.ModelForm):
    class Meta:
        model = Chairs
        fields = ['lab_name', 'categories1', 'categories2', 'categories3', 'status']


class TableForm(forms.ModelForm):
    class Meta:
        model = Tables
        fields = ['lab_name', 'categories1', 'categories2', 'status']

