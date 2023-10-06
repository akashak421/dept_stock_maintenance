from django import forms
from .models import Chairs, Tables, Board ,Cupboard,Mouse,Keyboard,Camera
from .models import TubeLight,Fan

class ChairForm(forms.ModelForm):
    class Meta:
        model = Chairs
        fields = ['lab_name', 'category1', 'category2', 'category3', 'status']


class TableForm(forms.ModelForm):
    class Meta:
        model = Tables
        fields = ['lab_name', 'category1', 'category2', 'status']

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['lab_name', 'category1', 'category2', 'category3','status']

class CupBoardForm(forms.ModelForm):
    class Meta:
        model = Cupboard
        fields = ['lab_name', 'category1', 'category2', 'category3','status']

class KeyboardForm(forms.ModelForm):
    class Meta:
        model = Keyboard
        fields = ['lab_name', 'category1', 'brand','status']


class MouseForm(forms.ModelForm):
    class Meta:
        model = Mouse
        fields = ['lab_name', 'category1', 'brand','status']

class CameraForm(forms.ModelForm):
    class Meta:
        model = Camera
        fields = ['lab_name', 'category1', 'brand','status']


#------------------form for electrical items------------

class TubeLightForm(forms.ModelForm):
    class Meta:
        model = TubeLight
        fields = ['lab_name','category1','status']

class FanForm(forms.ModelForm):
    class Meta:
        model = Fan
        fields = ['lab_name','category1','status']

class CctvForm(forms.ModelForm):
    class Meta:
        model = Cctv
        fields = ['lab_name','category1','category2','status']

