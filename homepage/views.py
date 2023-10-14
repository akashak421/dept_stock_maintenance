from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View
from django.contrib import messages

from .forms import BiometricForm, CameraForm, CctvForm, ChairForm, Connecting_WireForm, CpuForm, Extension_BoxForm, FanForm, MonitorForm, MouseForm, Network_SwitchForm, PrinterForm, Projector_ScreenForm, ProjectorForm, SocketForm,TableForm,BoardForm,CupBoardForm,KeyboardForm, TubeLightForm


from homepage.models import Category, Item, Chairs, Tables, Projector, Printer, Network_Switch, Projector_Screen


class HomeView(View):
    template_name = "home.html"
    def get(self, request):
        image_urls = [
        'images/islab.jpeg',
        'images/ibmlab.jpeg',
        'images/cclab.jpeg',
        'images/projectlab.jpeg',
        'images/researchlab.jpeg'
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
            messages.success(request, 'You have successfully added the item.')
            form = form_class()
            # Clear the form by redirecting to the same page
            return redirect('add_item_form',item_id=item_id)
    else:
        form = form_class()

    # If the form was not submitted or there are form errors, do not clear the form
    if not request.method == 'POST' or form.errors:
        form.novalidate = True

    return render(request, 'additemform.html',{'item': item,'form': form})


def research_lab(request):
    lab=research_lab
    # Calculate counts for different item categories
    chair_count = Chairs.objects.filter(lab_name=lab).count()
    table_count = Tables.objects.filter(lab_name=lab).count()
    projector_count = Projector.objects.filter(lab_name=lab).count()
    printer_count = Printer.objects.filter(lab_name=lab).count()
    switch_count = Network_Switch.objects.filter(lab_name=lab).count()
    screen_count = Projector_Screen.objects.filter(lab_name=lab).count()

    return render(request, 'reserach_lab.html', {
        'lab': lab,
        'chair_count': chair_count,
        'table_count': table_count,
        'projector_count': projector_count,
        'printer_count': printer_count,
        'switch_count': switch_count,
        'screen_count': screen_count,
    })
def project_lab(request):
    lab='cc'
    # Calculate counts for different item categories
    chair_count = Chairs.objects.filter(lab_name=lab).count()
    table_count = Tables.objects.filter(lab_name=lab).count()
    projector_count = Projector.objects.filter(lab_name=lab).count()
    printer_count = Printer.objects.filter(lab_name=lab).count()
    switch_count = Network_Switch.objects.filter(lab_name=lab).count()
    screen_count = Projector_Screen.objects.filter(lab_name=lab).count()

    return render(request, 'project_lab.html', {
        'lab': lab,
        'chair_count': chair_count,
        'table_count': table_count,
        'projector_count': projector_count,
        'printer_count': printer_count,
        'switch_count': switch_count,
        'screen_count': screen_count,
    })
def ibm_lab(request):
    lab='ibm'
    # Calculate counts for different item categories
    chair_count = Chairs.objects.filter(lab_name=lab).count()
    table_count = Tables.objects.filter(lab_name=lab).count()
    projector_count = Projector.objects.filter(lab_name=lab).count()
    printer_count = Printer.objects.filter(lab_name=lab).count()
    switch_count = Network_Switch.objects.filter(lab_name=lab).count()
    screen_count = Projector_Screen.objects.filter(lab_name=lab).count()

    return render(request, 'ibm_lab.html', {
        'lab': lab,
        'chair_count': chair_count,
        'table_count': table_count,
        'projector_count': projector_count,
        'printer_count': printer_count,
        'switch_count': switch_count,
        'screen_count': screen_count,
    })
def is_lab(request):
    lab='is'
    # Calculate counts for different item categories
    chair_count = Chairs.objects.filter(lab_name=lab).count()
    table_count = Tables.objects.filter(lab_name=lab).count()
    projector_count = Projector.objects.filter(lab_name=lab).count()
    printer_count = Printer.objects.filter(lab_name=lab).count()
    switch_count = Network_Switch.objects.filter(lab_name=lab).count()
    screen_count = Projector_Screen.objects.filter(lab_name=lab).count()

    return render(request, 'is_lab.html', {
        'lab': lab,
        'chair_count': chair_count,
        'table_count': table_count,
        'projector_count': projector_count,
        'printer_count': printer_count,
        'switch_count': switch_count,
        'screen_count': screen_count,
    })
def cc_lab(request):
    lab='cc'
    # Calculate counts for different item categories
    chair_count = Chairs.objects.filter(lab_name=lab).count()
    table_count = Tables.objects.filter(lab_name=lab).count()
    projector_count = Projector.objects.filter(lab_name=lab).count()
    printer_count = Printer.objects.filter(lab_name=lab).count()
    switch_count = Network_Switch.objects.filter(lab_name=lab).count()
    screen_count = Projector_Screen.objects.filter(lab_name=lab).count()

    return render(request, 'cc_lab.html', {
        'lab': lab,
        'chair_count': chair_count,
        'table_count': table_count,
        'projector_count': projector_count,
        'printer_count': printer_count,
        'switch_count': switch_count,
        'screen_count': screen_count,
    })