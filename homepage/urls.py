from django.urls import path

from core import settings
from django.conf.urls.static import static

# from django.conf.urls import url
from . import views

# app_name= 'items'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('additems/', views.add_items, name='add_items'),
    path('updateitems/<str:lab>/<int:item_id>/', views.update_items, name='update_items'),
    path('add/<int:category_id>/', views.item_list, name='item_list'),
    path('fetchdate/', views.fetch_date, name='fetch_date'),
    path('displaydata/', views.display_date, name='display_date'),
    # path('update/<int:category_id>/', views.update_item_list, name='update_item_list'),
    path('add_item_form/<int:item_id>/', views.add_item_form, name='add_item_form'),
    # path('update_item_form/<int:item_id>/', views.update_item_form, name='update_item_form'),
    path('update/',views.update, name='update'),
    path('lab/<str:lab>/', views.lab_view, name='lab_view'),
    path('<str:lab>/', views.generate_pdf, name='generate_pdf'),
    

    # path('update/',views.update, name='update'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)