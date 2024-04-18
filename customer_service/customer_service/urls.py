from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('requests/',include('service_requests.urls')),
    # path('status/', include('status.urls')),
]
