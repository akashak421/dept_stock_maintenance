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
    path('lab/researchlab/', views.research_lab, name='research_lab'),
    path('lab/projectlab/', views.project_lab, name='project_lab'),
    path('lab/islab/', views.is_lab, name='is_lab'),
    path('lab/ibmlab/', views.ibm_lab, name='ibm_lab'),
    path('lab/cclab/', views.cc_lab, name='cc_lab'),

    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)