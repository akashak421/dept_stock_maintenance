from django.urls import path
# from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('additems/', views.Add_ItemsView.as_view(), name='add_Items'),
]