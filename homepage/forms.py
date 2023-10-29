from django import forms
from .models import Item, Cctv, Chairs, Cpu, Extension_Box, Monitor, Network_Switch, Printer, Projector, Projector_Screen, Socket, Tables, Board ,Cupboard,Mouse,Keyboard,Camera,TubeLight,Fan,Connecting_Wire,Biometric


class ChairForm(forms.ModelForm):
    class Meta:
        model = Chairs
        fields = ['lab_name', 'arm_type', 'material_type', 'roll_type']


class TableForm(forms.ModelForm):
    class Meta:
        model = Tables
        fields = ['lab_name', 'table_type', 'material_type']

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['lab_name', 'board_type', 'material_type', 'installation_type']

class CupBoardForm(forms.ModelForm):
    class Meta:
        model = Cupboard
        fields = ['lab_name', 'cupboard_type', 'size', 'door_type']

class KeyboardForm(forms.ModelForm):
    class Meta:
        model = Keyboard
        fields = ['lab_name', 'keyboard_type', 'brand']


class MouseForm(forms.ModelForm):
    class Meta:
        model = Mouse
        fields = ['lab_name', 'mouse_type', 'brand']

class CameraForm(forms.ModelForm):
    class Meta:
        model = Camera
        fields = ['lab_name', 'web_cam_type', 'brand']


#------------------form for electrical items------------

class TubeLightForm(forms.ModelForm):
    class Meta:
        model = TubeLight
        fields = ['lab_name','light_type']

class FanForm(forms.ModelForm):
    class Meta:
        model = Fan
        fields = ['lab_name','fan_type']

class CctvForm(forms.ModelForm):
    class Meta:
        model = Cctv
        fields = ['lab_name','camera_type','camera_mode']

class BiometricForm(forms.ModelForm):
    class Meta:
        model = Biometric
        fields = ['lab_name','biometric_type','brand','model']


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
        fields = ['lab_name','switch_type','brand','model']

#----------------------------form of miscelleneous------------------------

class ProjectorForm(forms.ModelForm):
    class Meta:
        model = Projector
        fields = ['lab_name','brand','mounting_options']

class PrinterForm(forms.ModelForm):
    class Meta:
        model = Printer
        fields = ['lab_name','brand','model']

class SocketForm(forms.ModelForm):
    class Meta:
        model = Socket
        fields = ['lab_name','material_type','model','capacity']

class Projector_ScreenForm(forms.ModelForm):
    class Meta:
        model = Projector_Screen
        fields = ['lab_name','brand']

class Extension_BoxForm(forms.ModelForm):
    class Meta:
        model = Extension_Box
        fields = ['lab_name','material_type','model','ampere_rating']

class Connecting_WireForm(forms.ModelForm):
    class Meta:
        model = Connecting_Wire
        fields = ['lab_name','wire_type','quantity']

#----------------------------update form--------------------------------------------------------
class Update_ChairForm(forms.ModelForm):
    class Meta:
        model = Chairs
        fields = ['lab_name','id', 'arm_type', 'material_type', 'roll_type','status']
    lab_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

class Update_TableForm(forms.ModelForm):
    class Meta:
        model = Tables
        fields = ['lab_name','id', 'table_type', 'material_type','status']
    lab_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

class Update_BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['lab_name','id', 'board_type', 'material_type', 'installation_type','status']
    lab_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

class Update_CupBoardForm(forms.ModelForm):
    class Meta:
        model = Cupboard
        fields = ['lab_name','id', 'cupboard_type', 'size', 'door_type','status']
    lab_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

class Update_KeyboardForm(forms.ModelForm):
    class Meta:
        model = Keyboard
        fields = ['lab_name','id', 'keyboard_type', 'brand','status']
    lab_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

class Update_MouseForm(forms.ModelForm):
    class Meta:
        model = Mouse
        fields = ['lab_name','id', 'mouse_type', 'brand','status']
    lab_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

class Update_CameraForm(forms.ModelForm):
    class Meta:
        model = Camera
        fields = ['lab_name','id', 'web_cam_type', 'brand','status']
    lab_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))


#------------------form for electrical items------------

class Update_TubeLightForm(forms.ModelForm):
    class Meta:
        model = TubeLight
        fields = ['lab_name','id','light_type','status']
    lab_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

class Update_FanForm(forms.ModelForm):
    class Meta:
        model = Fan
        fields = ['lab_name','id','fan_type','status']
    lab_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

class Update_CctvForm(forms.ModelForm):
    class Meta:
        model = Cctv
        fields = ['lab_name','id','camera_type','camera_mode','status']
    lab_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

class Update_BiometricForm(forms.ModelForm):
    class Meta:
        model = Biometric
        fields = ['lab_name','id','biometric_type','brand','model','status']
    lab_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

#------------------------form of capital equipments--------------------

class Update_MonitorForm(forms.ModelForm):
    class Meta:
        model = Monitor
        fields = ['lab_name','id','brand','model','status']
    lab_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

class Update_CpuForm(forms.ModelForm):
    class Meta:
        model = Cpu
        fields = ['lab_name','id','brand','status']
    lab_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

class Update_Network_SwitchForm(forms.ModelForm):
    class Meta:
        model = Network_Switch
        fields = ['lab_name','id','switch_type','brand','model','status']
    lab_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

#----------------------------form of miscelleneous------------------------

class Update_ProjectorForm(forms.ModelForm):
    class Meta:
        model = Projector
        fields = ['lab_name','id','brand','mounting_options','status']
    lab_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

class Update_PrinterForm(forms.ModelForm):
    class Meta:
        model = Printer
        fields = ['lab_name','id','brand','model','status']
    lab_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

class Update_SocketForm(forms.ModelForm):
    class Meta:
        model = Socket
        fields = ['lab_name','id','material_type','model','capacity','status']
    lab_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

class Update_Projector_ScreenForm(forms.ModelForm):
    class Meta:
        model = Projector_Screen
        fields = ['lab_name','id','brand','status']
    lab_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

class Update_Extension_BoxForm(forms.ModelForm):
    class Meta:
        model = Extension_Box
        fields = ['lab_name','id','material_type','model','ampere_rating','status']
    lab_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

class Update_Connecting_WireForm(forms.ModelForm):
    class Meta:
        model = Connecting_Wire
        fields = ['lab_name','id','wire_type','quantity','status']
    lab_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

