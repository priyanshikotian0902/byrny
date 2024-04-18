# status/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('status/', views.status_change_list, name='status_change_list'),
    path('status/<int:status_change_id>/', views.status_change_detail, name='status_change_detail'),
]
