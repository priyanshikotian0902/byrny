from django.db import models
from django.utils import timezone
from service_requests.models import ServiceRequest

class ServiceRequestStatusChange(models.Model):
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE)
    old_status = models.CharField(max_length=20)
    new_status = models.CharField(max_length=20)
    timestamp = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Status change for {self.service_request} from {self.old_status} to {self.new_status}"
