from django import forms
from .models import Cctv, Chairs, Cpu, Extension_Box, Monitor, Network_Switch, Printer, Projector, Projector_Screen, Socket, Tables, Board ,Cupboard,Mouse,Keyboard,Camera,TubeLight,Fan,Connecting_Wire,Biometric


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
        fields = ['id','lab_name', 'arm_type', 'material_type', 'roll_type','status']


class Update_TableForm(forms.ModelForm):
    class Meta:
        model = Tables
        fields = ['id','lab_name', 'table_type', 'material_type','status']

class Update_BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['id','lab_name', 'board_type', 'material_type', 'installation_type','status']

class Update_CupBoardForm(forms.ModelForm):
    class Meta:
        model = Cupboard
        fields = ['id','lab_name', 'cupboard_type', 'size', 'door_type','status']

class Update_KeyboardForm(forms.ModelForm):
    class Meta:
        model = Keyboard
        fields = ['id','lab_name', 'keyboard_type', 'brand','status']


class Update_MouseForm(forms.ModelForm):
    class Meta:
        model = Mouse
        fields = ['id','lab_name', 'mouse_type', 'brand','status']

class Update_CameraForm(forms.ModelForm):
    class Meta:
        model = Camera
        fields = ['id','lab_name', 'web_cam_type', 'brand','status']


#------------------form for electrical items------------

class Update_TubeLightForm(forms.ModelForm):
    class Meta:
        model = TubeLight
        fields = ['id','lab_name','light_type','status']

class Update_FanForm(forms.ModelForm):
    class Meta:
        model = Fan
        fields = ['id','lab_name','fan_type','status']

class Update_CctvForm(forms.ModelForm):
    class Meta:
        model = Cctv
        fields = ['id','lab_name','camera_type','camera_mode','status']

class Update_BiometricForm(forms.ModelForm):
    class Meta:
        model = Biometric
        fields = ['id','lab_name','biometric_type','brand','model','status']


#------------------------form of capital equipments--------------------

class Update_MonitorForm(forms.ModelForm):
    class Meta:
        model = Monitor
        fields = ['id','lab_name','brand','model','status']

class Update_CpuForm(forms.ModelForm):
    class Meta:
        model = Cpu
        fields = ['id','lab_name','brand','status']

class Update_Network_SwitchForm(forms.ModelForm):
    class Meta:
        model = Network_Switch
        fields = ['id','lab_name','switch_type','brand','model','status']

#----------------------------form of miscelleneous------------------------

class Update_ProjectorForm(forms.ModelForm):
    class Meta:
        model = Projector
        fields = ['id','lab_name','brand','mounting_options','status']

class Update_PrinterForm(forms.ModelForm):
    class Meta:
        model = Printer
        fields = ['id','lab_name','brand','model','status']

class Update_SocketForm(forms.ModelForm):
    class Meta:
        model = Socket
        fields = ['id','lab_name','material_type','model','capacity','status']

class Update_Projector_ScreenForm(forms.ModelForm):
    class Meta:
        model = Projector_Screen
        fields = ['id','lab_name','brand','status']

class Update_Extension_BoxForm(forms.ModelForm):
    class Meta:
        model = Extension_Box
        fields = ['id','lab_name','material_type','model','ampere_rating','status']

class Update_Connecting_WireForm(forms.ModelForm):
    class Meta:
        model = Connecting_Wire
        fields = ['id','lab_name','wire_type','quantity','status']

