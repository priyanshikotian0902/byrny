# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_service_request, name='submit_service_request'),
    path('account/', views.view_account, name='view_account'),
]
