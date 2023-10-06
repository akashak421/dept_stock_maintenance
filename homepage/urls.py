from django.urls import path

from core import settings
from django.conf.urls.static import static

# from django.conf.urls import url
from . import views

# app_name= 'items'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('additems/', views.add_items, name='add_items'),
    path('<int:category_id>/', views.item_list, name='item_list'),
    path('add_item_form/<int:item_id>/', views.add_item_form, name='add_item_form'),
    
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)