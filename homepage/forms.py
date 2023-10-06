from django import forms
from .models import Chairs

class ItemForm(forms.ModelForm):
    class Meta:
        model = Chairs
        fields = ['name', 'lab_name', 'categories1', 'categories2', 'categories3', 'status']
