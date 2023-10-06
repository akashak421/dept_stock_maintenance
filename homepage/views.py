from multiprocessing import context
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View
from .forms import ChairForm,TableForm,BoardForm


from homepage.models import Category, Item


class HomeView(View):
    template_name = "home.html"
    def get(self, request):
        return render(request,'home.html')

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
    if item_id == 15:
        form_class = ChairForm
    elif item_id == 16:
        form_class = TableForm
    elif item_id == 10:
        form_class = BoardForm

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            form = form_class()
            # Clear the form by redirecting to the same page
            return redirect('add_item_form', item_id=item_id)
    else:
        form = form_class()

    # If the form was not submitted or there are form errors, do not clear the form
    if not request.method == 'POST' or form.errors:
        form.novalidate = True

    return render(request, 'additemform.html', {'form': form})
