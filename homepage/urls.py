from django.urls import path
# from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('additems/', views.add_items, name='add_items'),
    path('<int:category_id>/', views.item_list, name='item_list'),
]