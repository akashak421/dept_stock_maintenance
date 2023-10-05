from multiprocessing import context
from django.shortcuts import render
from django.views.generic import View, TemplateView
# from inventory.models import Stock
# from transactions.models import SaleBill, PurchaseBill


class HomeView(View):
    template_name = "home.html"
    def get(self, request):
        return render(request,'home.html')

class Add_ItemsView(View):
    template_name = "addItems.html"