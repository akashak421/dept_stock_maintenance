from django import forms
from .models import Cctv, Chairs, Cpu, Extension_Box, Monitor, Network_Switch, Printer, Projector, Projector_Screen, Socket, Tables, Board ,Cupboard,Mouse,Keyboard,Camera,TubeLight,Fan,Connecting_Wire,Biometric


class ChairForm(forms.ModelForm):
    class Meta:
        model = Chairs
        fields = ['lab_name', 'armtype', 'material', 'rolltype']


class TableForm(forms.ModelForm):
    class Meta:
        model = Tables
        fields = ['lab_name', 'category1', 'category2']

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['lab_name', 'category1', 'category2', 'category3']

class CupBoardForm(forms.ModelForm):
    class Meta:
        model = Cupboard
        fields = ['lab_name', 'category1', 'category2', 'category3']

class KeyboardForm(forms.ModelForm):
    class Meta:
        model = Keyboard
        fields = ['lab_name', 'category1', 'brand']


class MouseForm(forms.ModelForm):
    class Meta:
        model = Mouse
        fields = ['lab_name', 'category1', 'brand']

class CameraForm(forms.ModelForm):
    class Meta:
        model = Camera
        fields = ['lab_name', 'category1', 'brand']


#------------------form for electrical items------------

class TubeLightForm(forms.ModelForm):
    class Meta:
        model = TubeLight
        fields = ['lab_name','category1']

class FanForm(forms.ModelForm):
    class Meta:
        model = Fan
        fields = ['lab_name','category1']

class CctvForm(forms.ModelForm):
    class Meta:
        model = Cctv
        fields = ['lab_name','category1','category2']

class BiometricForm(forms.ModelForm):
    class Meta:
        model = Biometric
        fields = ['lab_name','category1','brand','model']


#------------------------form of capital equipments--------------------

class MonitorForm(forms.ModelForm):
    class Meta:
        model = Monitor
        fields = ['lab_name','brand','model']

class CpuForm(forms.ModelForm):
    class Meta:
        model = Cpu
        fields = ['lab_name','brand']

class Network_SwitchForm(forms.ModelForm):
    class Meta:
        model = Network_Switch
        fields = ['lab_name','category1','category2','brand']

#----------------------------form of miscelleneous------------------------

class ProjectorForm(forms.ModelForm):
    class Meta:
        model = Projector
        fields = ['lab_name','brand','Mounting_Options']

class PrinterForm(forms.ModelForm):
    class Meta:
        model = Printer
        fields = ['lab_name','brand','model']

class SocketForm(forms.ModelForm):
    class Meta:
        model = Socket
        fields = ['lab_name','category1','category2','category3']

class Projector_ScreenForm(forms.ModelForm):
    class Meta:
        model = Projector_Screen
        fields = ['lab_name','category1','brand']

class Extension_BoxForm(forms.ModelForm):
    class Meta:
        model = Extension_Box
        fields = ['lab_name','category1','category2','category3']

class Connecting_WireForm(forms.ModelForm):
    class Meta:
        model = Connecting_Wire
        fields = ['lab_name','category1','quantity']

