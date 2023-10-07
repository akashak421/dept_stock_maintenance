from django import forms
from .models import Chairs, Tables, Board ,Cupboard,Mouse,Keyboard,Camera
from .models import TubeLight,Fan,Cctv,Biometric
from .models import Monitor,Cpu,Network_Switch
from .models import Projector,Printer,Socket

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

class BiometricForm(forms.ModelForm):
    class Meta:
        model = Biometric
        fields = ['lab_name','category1','brand','model','status']


#------------------------form of capital equipments--------------------

class MonitorForm(forms.ModelForm):
    class Meta:
        model = Monitor
        fields = ['lab_name','brand','model','status']

class CpuForm(forms.ModelForm):
    class Meta:
        model = Cpu
        fields = ['lab_name','brand','status']

class Network_SwitchForm(forms.ModelForm):
    class Meta:
        model = Network_Switch
        fields = ['lab_name','category1','category2','brand','status']

#----------------------------form of miscelleneous------------------------

class ProjectorForm(forms.ModelForm):
    class Meta:
        model = Projector
        fields = ['lab_name','brand','Mounting_Options','status']

class PrinterForm(forms.ModelForm):
    class Meta:
        model = Printer
        fields = ['lab_name','brand','model','status']

class SocketForm(forms.ModelForm):
    class Meta:
        model = Socket
        fields = ['lab_name','category1','category2','category3','status']

class Projector_ScreenForm(forms.ModelForm):
    class Meta:
        model = Projector_Screen
        fields = ['lab_name','category1','brand','status']

class Extension_BoxForm(forms.ModelForm):
    class Meta:
        model = Extension_Box
        fields = ['lab_name','category1','category2','category3','status']

class Connecting_WireForm(forms.ModelForm):
    class Meta:
        model = Connecting_Wire
        fields = ['lab_name','category1','quantity','status']

