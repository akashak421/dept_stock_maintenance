from django import forms
from .models import Chairs

class ChairForm(forms.ModelForm):
    class Meta:
        model = Chairs
        fields = ['lab_name', 'category1', 'category2', 'category3', 'status']

class ChairForm(forms.ModelForm):
    class Meta:
        model = Tables
        fields = ['lab_name', 'category1', 'category2', 'category3', 'status']