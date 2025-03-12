from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:day_id>/', views.edit_day, name='edit_day'),
    path('search/', views.search, name='search'),
    path('export/', views.export, name='export'),
]