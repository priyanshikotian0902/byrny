from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .serializers import ServiceRequestSerializer
from django.contrib.auth.decorators import login_required
from accounts.models import CustomerProfile
from .models import ServiceRequest
import json

@csrf_exempt
def submit_service_request(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            if 'attachment' not in data or not isinstance(data['attachment'], str):
                return JsonResponse({'error': 'Please submit the attachment filename as a string'}, status=400)

            customer_profile = CustomerProfile.objects.get(id=data['customer'])

            service_request = ServiceRequest.objects.create(
                customer=customer_profile,
                type=data['type'],
                details=data['details'],
                attachment=data['attachment']
            )

            if 'status' in data:
                service_request.status = data['status']
                service_request.save()
            return JsonResponse({'message': 'Service request submitted successfully'}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        except CustomerProfile.DoesNotExist:
            return JsonResponse({'error': 'Customer profile does not exist'}, status=400)
    else:
        return JsonResponse({'message': 'Displaying form for submitting service request'})




@login_required
def view_account(request):

    user_profile = request.user.customer_profile


    account_info = {
        'email': user_profile.email,
        'username': user_profile.username,

    }


    try:
        user_address = Address.objects.get(customer=user_profile)
        address_info = {
            'street': user_address.street,
            'city': user_address.city,
            'state': user_address.state,
            'country': user_address.country,
            'postal_code': user_address.postal_code,
        }
    except Address.DoesNotExist:
        # Handle case where address does not exist
        address_info = None


    message = f"Account Information:\nEmail: {account_info['email']}\nUsername: {account_info['username']}\n"
    if address_info:
        message += "\nAddress Information:\n"
        for key, value in address_info.items():
            message += f"{key.capitalize()}: {value}\n"
    else:
        message += "\nNo address on file."

    return JsonResponse({'message': message})
