from multiprocessing import context
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View
from .forms import ChairForm,TableForm


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


def add_item_chair(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    form = None

    # Define which form to use based on item_id
    if item_id == 15:
        form = ChairForm(request.POST or None)
    elif item_id == 1:
        form = TableForm(request.POST or None)

    if request.method == 'POST':
        if form is not None:
            if form.is_valid():
                form.save()
                # You can customize the response based on your requirements
                return render(request, 'additemchair.html', {'form': form})

    return render(request, 'additemchair.html', {'form': form})

