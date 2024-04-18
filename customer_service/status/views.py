
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ServiceRequestStatusChange
import json

@csrf_exempt
def status_change_list(request):
    if request.method == 'GET':
        status_changes = ServiceRequestStatusChange.objects.all()
        data = [{'id': status_change.id, 'service_request': str(status_change.service_request), 'old_status': status_change.old_status,
                 'new_status': status_change.new_status, 'timestamp': status_change.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                 'description': status_change.description} for status_change in status_changes]
        return JsonResponse(data, safe=False)
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            service_request_id = data.get('service_request_id')
            old_status = data.get('old_status')
            new_status = data.get('new_status')
            description = data.get('description')
            service_request = ServiceRequest.objects.get(id=service_request_id)
            status_change = ServiceRequestStatusChange.objects.create(service_request=service_request, old_status=old_status,
                                                                      new_status=new_status, description=description)
            return JsonResponse({'message': 'Status change created successfully', 'status_change_id': status_change.id}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        except ServiceRequest.DoesNotExist:
            return JsonResponse({'error': 'Service request does not exist'}, status=400)

@csrf_exempt
def status_change_detail(request, status_change_id):
    if request.method == 'GET':
        try:
            status_change = ServiceRequestStatusChange.objects.get(id=status_change_id)
            data = {'id': status_change.id, 'service_request': str(status_change.service_request), 'old_status': status_change.old_status,
                    'new_status': status_change.new_status, 'timestamp': status_change.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                    'description': status_change.description}
            return JsonResponse(data)
        except ServiceRequestStatusChange.DoesNotExist:
            return JsonResponse({'error': 'Status change does not exist'}, status=404)
    elif request.method == 'DELETE':
        try:
            status_change = ServiceRequestStatusChange.objects.get(id=status_change_id)
            status_change.delete()
            return JsonResponse({'message': 'Status change deleted successfully'})
        except ServiceRequestStatusChange.DoesNotExist:
            return JsonResponse({'error': 'Status change does not exist'}, status=404)



