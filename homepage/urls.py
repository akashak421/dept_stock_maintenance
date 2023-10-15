from django.urls import path

from core import settings
from django.conf.urls.static import static

# from django.conf.urls import url
from . import views

# app_name= 'items'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('additems/', views.add_items, name='add_items'),
    path('updateitems/', views.update_items, name='update_items'),
    path('add/<int:category_id>/', views.item_list, name='item_list'),
    path('update/<int:category_id>/', views.update_item_list, name='update_item_list'),
    path('add_item_form/<int:item_id>/', views.add_item_form, name='add_item_form'),
    path('update_item_form/<int:item_id>/', views.update_item_form, name='update_item_form'),
     path('lab/<str:lab>/', views.lab_view, name='lab_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)