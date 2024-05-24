from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_list/', views.create_list, name='create_list'),
    path('add_item/<int:list_id>/', views.add_item, name='add_item'),
    path('list_items/', views.list_items, name='list_items'),
]
