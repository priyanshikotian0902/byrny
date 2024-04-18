# customer_service/models.py
from django.db import models
from accounts.models import CustomerProfile

class ServiceRequest(models.Model):
    customer = models.ForeignKey(CustomerProfile, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    details = models.TextField()
    attachment = models.FileField(upload_to='service_request_attachments/')
    status = models.CharField(max_length=20, default='Pending')

