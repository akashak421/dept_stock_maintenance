from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View
from django.contrib import messages
from itertools import product
from django.http import Http404, HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django import forms



from .forms import BiometricForm, CameraForm, CctvForm, ChairForm, Connecting_WireForm, CpuForm, Extension_BoxForm, FanForm, MonitorForm, MouseForm, Network_SwitchForm, PrinterForm, Projector_ScreenForm, ProjectorForm, SocketForm,TableForm,BoardForm,CupBoardForm,KeyboardForm, TubeLightForm
from .forms import Update_BiometricForm, Update_CameraForm, Update_CctvForm, Update_ChairForm, Update_Connecting_WireForm, Update_CpuForm, Update_Extension_BoxForm, Update_FanForm, Update_MonitorForm, Update_MouseForm, Update_Network_SwitchForm, Update_PrinterForm, Update_Projector_ScreenForm, Update_ProjectorForm, Update_SocketForm,Update_TableForm,Update_BoardForm,Update_CupBoardForm,Update_KeyboardForm, Update_TubeLightForm

from homepage.models import Category, Item, Chairs, Tables, Projector, Printer, Network_Switch, Projector_Screen, Fan, TubeLight,Cctv,Biometric,Keyboard,Mouse,Camera,Board,Cupboard,Monitor,Cpu,Socket,Extension_Box,Connecting_Wire


class HomeView(View):
    template_name = "home.html"
    def get(self, request):
        image_urls = [
        'images/islab.jpeg',
        'images/ibmlab.jpeg',
        'images/cclab.jpeg',
        'images/projectlab.jpeg',
        'images/wirelesslab.jpeg'
    ]
        return render(request, 'home.html', {'image_urls': image_urls})

def add_items(request):
    categories = Category.objects.all()  # Get all categories
    return render(request, 'additems.html', {'categories': categories})


def item_list(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    items = Item.objects.filter(category=category)
    return render(request, 'itemlist.html', {'category': category, 'items': items})


def add_item_form(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    form = None

    # Define which form to use based on item_id
    if item_id == 1:
        form_class = TableForm
    elif item_id == 2:
        form_class = ChairForm
    elif item_id == 3:
        form_class = TubeLightForm
    elif item_id == 4:
        form_class = FanForm
    elif item_id == 5:
        form_class = CctvForm
    elif item_id == 6:
        form_class = BiometricForm
    elif item_id == 7:
        form_class = KeyboardForm
    elif item_id == 8:
        form_class = MouseForm
    elif item_id == 9:
        form_class = CameraForm
    elif item_id == 10:
        form_class = BoardForm
    elif item_id == 11:
        form_class = CupBoardForm
    elif item_id == 12:
        form_class = MonitorForm
    elif item_id == 13:
        form_class = CpuForm
    elif item_id == 14:
        form_class = Network_SwitchForm
    elif item_id == 15:
        form_class = ProjectorForm
    elif item_id == 16:
        form_class = PrinterForm
    elif item_id == 17:
        form_class = SocketForm
    elif item_id == 18:
        form_class = Projector_ScreenForm
    elif item_id == 19:
        form_class = Extension_BoxForm
    elif item_id == 20:
        form_class = Connecting_WireForm
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'You have successfully added the item.')
            show_success_message = True
            form = form_class()
            # Clear the form by redirecting to the same page
            return redirect('add_item_form',item_id=item_id)
    else:
        form = form_class()
    if not request.method == 'POST' or form.errors:
        form.novalidate = True

    return render(request, 'additemform.html',{'item': item,'form': form})

def update(request):
    items = Item.objects.all()
    if request.method == 'POST':
        # Form submission logic
        lab = request.POST.get('lab')
        item_id = request.POST.get('item')
        return redirect('update_items', lab=lab, item_id=item_id)
    return render(request, 'update.html',{'items':items})

def update_items(request, lab, item_id):
    item_name = Item.objects.filter(id=item_id).values_list('name', flat=True).first()

    model_name_mapping = {
        "TubeLight": "TubeLight",
        "Fan": "Fan",
        "Chair": "Chairs",
        "Extension Box": "Extension_box",
        "Connecting Wires": "Connecting_wire",
        "Table": "Tables",
        "CCTV": "Cctv",
        "Biometric":"Biometric",
        "Board":"Board",
        "Camera":"Camera",
        "CPU":"Cpu",
        "Cupboard":"Cupboard",
        "Keyboard":"Keyboard",
        "Monitor":"Monitor",
        "Mouse":"Mouse",
        "Network switch":"Network_switch",
        "Printer":"Printer",
        "Projector":"Projector",
        "Screen":"Projector_screen",
        "Socket":"Socket"
        }

    model_name = model_name_mapping.get(item_name)

    try:
        item_model = globals()[model_name]
        filtered_ids = item_model.objects.filter(lab_name=lab).values_list('id', flat=True)
    except KeyError:
        filtered_ids = []
    print(model_name)
    print(filtered_ids)

    form_classes = {
        1: Update_TableForm,
        2: Update_ChairForm,
        3: Update_TubeLightForm,
        4: Update_FanForm,
        5: Update_CctvForm,
        6: Update_BiometricForm,
        7: Update_KeyboardForm,
        8: Update_MouseForm,
        9: Update_CameraForm,
        10: Update_BoardForm,
        11: Update_CupBoardForm,
        12: Update_MonitorForm,
        13: Update_CpuForm,
        14: Update_Network_SwitchForm,
        15: Update_ProjectorForm,
        16: Update_PrinterForm,
        17: Update_SocketForm,
        18: Update_Projector_ScreenForm,
        19: Update_Extension_BoxForm,
        20: Update_Connecting_WireForm,
    }

    form_class = form_classes.get(item_id, None)
    initial_data = {
        'lab_name': lab,
    }

    if request.method == 'POST':
        form = form_class(request.POST)
        print(request.POST)
        if form.is_valid() or request.POST.get('submit_with_errors') == '1':
            selected_id = form.instance.id
            if item_model.objects.filter(id=selected_id).exists():
                try:
                    to_update = item_model.objects.get(id=selected_id)
                except item_model.DoesNotExist:
                    raise Http404("Item with the selected ID does not exist")
                for field_name, field_value in form.cleaned_data.items():
                    setattr(to_update, field_name, field_value)
                to_update.save()
                messages.success(request, 'The Item has been successfully updated')
            else:
                # Print or log a message to confirm that the ID doesn't exist
                print(f"Item with ID {selected_id} does not exist in the database")
        else:
            print(form.errors)
    else:
        form = form_class(initial=initial_data)

    if 'id' in form.fields:
        form.fields['id'].widget = forms.Select(choices=[(id, id) for id in filtered_ids])



    else:
        form = None

    return render(request, 'updateitems.html', {'item_name': item_name, 'lab': lab, 'item_id': item_id, 'form': form})

def lab_view(request, lab):
    template_name = f'{lab}.html'
    chair_count = Chairs.objects.filter(lab_name=lab).count()
    table_count = Tables.objects.filter(lab_name=lab).count()
    projector_count = Projector.objects.filter(lab_name=lab).count()
    printer_count = Printer.objects.filter(lab_name=lab).count()
    switch_count = Network_Switch.objects.filter(lab_name=lab).count()
    screen_count = Projector_Screen.objects.filter(lab_name=lab).count()
    biometric_count = Biometric.objects.filter(lab_name=lab).count()
    tubelight_count = TubeLight.objects.filter(lab_name=lab).count()
    fan_count = Fan.objects.filter(lab_name=lab).count()
    cctv_count = Cctv.objects.filter(lab_name=lab).count()
    keyboard_count = Keyboard.objects.filter(lab_name=lab).count()
    mouse_count = Mouse.objects.filter(lab_name=lab).count()
    camera_count = Camera.objects.filter(lab_name=lab).count()
    board_count = Board.objects.filter(lab_name=lab).count()
    cupboard_count = Cupboard.objects.filter(lab_name=lab).count()
    monitor_count = Monitor.objects.filter(lab_name=lab).count()
    cpu_count = Cpu.objects.filter(lab_name=lab).count()
    socket_count = Socket.objects.filter(lab_name=lab).count()
    extension_box_count = Extension_Box.objects.filter(lab_name=lab).count()
    connecting_wire_count = Connecting_Wire.objects.filter(lab_name=lab).count()

    # Define category options
    arm_categories = ['with_arm', 'without_arm']
    material_categories = ['plastic', 'wooden','steel','fiber']
    rolling_categories = ['rolling', 'non_rolling']

    # Initialize a dictionary to store counts for each combination
    chair_counts = {}

    # Generate all possible combinations
    combinations = product(material_categories, arm_categories, rolling_categories)

    # Loop through each combination and count chairs
    for combination in combinations:
        material_category,arm_category, rolling_category = combination

        # Count chairs for this combination
        count = Chairs.objects.filter(
            lab_name=lab,
            material_type=material_category,
            arm_type=arm_category,
            roll_type=rolling_category
        ).count()

        # Store the count in the dictionary with the combination as the key
        chair_counts[combination] = count

    # You can now access counts for various combinations like chair_counts[('with_arm', 'plastic', 'rolling')]

    return render(request, template_name, {
        'lab': lab,
        'chair_counts': chair_counts,
        'chair_count': chair_count,
        'table_count': table_count,
        'projector_count': projector_count,
        'printer_count': printer_count,
        'switch_count': switch_count,
        'screen_count': screen_count,
        'biometric_count' : biometric_count,
        'tubelight_count' : tubelight_count,
        'fan_count' : fan_count,
        'cctv_count' : cctv_count,
        'keyboard_count' : keyboard_count,
        'mouse_count' : mouse_count,
        'camera_count' : camera_count,
        'board_count' : board_count,
        'cupboard_count' : cupboard_count,
        'monitor_count' : monitor_count,
        'cpu_count' :cpu_count,
        'socket_count' : socket_count,
        'extension_box_count' : extension_box_count,
        'connecting_wire_count' : connecting_wire_count,
        
    })

def generate_pdf(request,lab):
    chair_count = Chairs.objects.filter(lab_name=lab).count()
    table_count = Tables.objects.filter(lab_name=lab).count()
    projector_count = Projector.objects.filter(lab_name=lab).count()
    printer_count = Printer.objects.filter(lab_name=lab).count()
    switch_count = Network_Switch.objects.filter(lab_name=lab).count()
    screen_count = Projector_Screen.objects.filter(lab_name=lab).count()
    biometric_count = Biometric.objects.filter(lab_name=lab).count()
    tubelight_count = TubeLight.objects.filter(lab_name=lab).count()
    fan_count = Fan.objects.filter(lab_name=lab).count()
    cctv_count = Cctv.objects.filter(lab_name=lab).count()
    keyboard_count = Keyboard.objects.filter(lab_name=lab).count()
    mouse_count = Mouse.objects.filter(lab_name=lab).count()
    camera_count = Camera.objects.filter(lab_name=lab).count()
    board_count = Board.objects.filter(lab_name=lab).count()
    cupboard_count = Cupboard.objects.filter(lab_name=lab).count()
    monitor_count = Monitor.objects.filter(lab_name=lab).count()
    cpu_count = Cpu.objects.filter(lab_name=lab).count()
    socket_count = Socket.objects.filter(lab_name=lab).count()
    extension_box_count = Extension_Box.objects.filter(lab_name=lab).count()
    connecting_wire_count = Connecting_Wire.objects.filter(lab_name=lab).count()
    total = chair_count + table_count +projector_count+printer_count+switch_count+screen_count+biometric_count+tubelight_count+fan_count+cctv_count+keyboard_count+mouse_count+camera_count+board_count+cupboard_count+monitor_count+cpu_count+socket_count+extension_box_count+connecting_wire_count

    Name_of_the_lab=lab.upper()
    pdf = render_to_pdf('pdf.html', {
        'Name_of_the_lab': Name_of_the_lab,
        'chair_count': chair_count,
        'table_count': table_count,
        'projector_count': projector_count,
        'printer_count': printer_count,
        'switch_count': switch_count,
        'screen_count': screen_count,
        'biometric_count' : biometric_count,
        'tubelight_count' : tubelight_count,
        'fan_count' : fan_count,
        'cctv_count' : cctv_count,
        'keyboard_count' : keyboard_count,
        'mouse_count' : mouse_count,
        'camera_count' : camera_count,
        'board_count' : board_count,
        'cupboard_count' : cupboard_count,
        'monitor_count' : monitor_count,
        'cpu_count' :cpu_count,
        'socket_count' : socket_count,
        'extension_box_count' : extension_box_count,
        'connecting_wire_count' : connecting_wire_count,
        'total' : total
    })

    return HttpResponse(pdf, content_type='application/pdf')

def render_to_pdf(template_path, context_dict):
    template = get_template(template_path)
    html = template.render(context_dict)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="lab_items_report.pdf"'

    # Generate PDF
    pisa_status = pisa.CreatePDF(html, dest=response)

    if pisa_status.err:
        return HttpResponse('We had some errors with code %s <pre>%s</pre>' % (pisa_status.err, html))
    return response


def display_date(request):
    if request.method == 'POST':
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')

        # Assuming your model has a DateTimeField called 'created_at' for the creation date
        # Filter records based on the selected date range
        table_records = Tables.objects.filter(created_at__range=[from_date, to_date])
        chair_records = Chairs.objects.filter(created_at__range=[from_date, to_date])
        cupboard_records = Cupboard.objects.filter(created_at__range=[from_date, to_date])
        keyboard_records = Keyboard.objects.filter(created_at__range=[from_date, to_date])
        Mouse_records = Mouse.objects.filter(created_at__range=[from_date, to_date])
        camera_records = Camera.objects.filter(created_at__range=[from_date, to_date])
        tubelight_records = TubeLight.objects.filter(created_at__range=[from_date, to_date])
        fan_records = Fan.objects.filter(created_at__range=[from_date, to_date])
        cctv_records = Cctv.objects.filter(created_at__range=[from_date, to_date])
        bio_records = Biometric.objects.filter(created_at__range=[from_date, to_date])
        monitor_records = Monitor.objects.filter(created_at__range=[from_date, to_date])
        cpu_records = Cpu.objects.filter(created_at__range=[from_date, to_date])
        Network_Switch_records = Network_Switch.objects.filter(created_at__range=[from_date, to_date])
        projector_records = Projector.objects.filter(created_at__range=[from_date, to_date])
        printer_records = Printer.objects.filter(created_at__range=[from_date, to_date])
        socket_records = Socket.objects.filter(created_at__range=[from_date, to_date])
        pro_screen_records = Projector_Screen.objects.filter(created_at__range=[from_date, to_date])
        ex_box_records = Extension_Box.objects.filter(created_at__range=[from_date, to_date])
        con_wire_records = Connecting_Wire.objects.filter(created_at__range=[from_date, to_date])

        board_records = Board.objects.filter(created_at__range=[from_date, to_date])
        chair_count = Chairs.objects.filter(created_at__range=[from_date, to_date]).count()

        # Calculate counts for various items
        # chair_count = records.filter(item_type='Chairs').count()
        # table_count = records.filter(item_type='Tables').count()
        # ... other item counts ...

        table_count = table_records.count()  # Total number of products

        context = {
            'Name_of_the_lab': 'Your Lab Name',
            'chair_count': chair_count,
            'board_records':board_records,
            'table_count': table_count,
            'table_records': table_records,
            'chair_records':chair_records,
            'cupboard_records':cupboard_records,
            'keyboard_records':keyboard_records,
            'Mouse_records':Mouse_records,
            'camera_records':camera_records,
            'tubelight_records':tubelight_records,
            'fan_records':fan_records,
            'cctv_records':cctv_records,
            'bio_records':bio_records,
            'monitor_records':monitor_records,
            'cpu_records':cpu_records,
            'Network_Switch_records':Network_Switch_records,
            'projector_records':projector_records,
            'printer_records':printer_records,
            'socket_records':socket_records,
            'pro_screen_records':pro_screen_records,
            'ex_box_records':ex_box_records,
            'con_wire_records':con_wire_records,
            
          
        }
        pdf = render_to_pdf('display_date.html',context)

        return HttpResponse(pdf, content_type='application/pdf')

        

    return render(request, 'display_date.html')

def fetch_date(request): 
    return render(request, 'fetch_date.html')



# def my_template_view(request):
#     return render(request, 'mytemplate.html')