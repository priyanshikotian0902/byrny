from rest_framework.views import APIView
from .models import CustomerProfile, Address
from .serializers import CustomerProfileSerializer, AddressSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class UserRegistrationAPIView(APIView):
    def post(self, request):

        customer_profile_serializer = CustomerProfileSerializer(data=request.data)


        if customer_profile_serializer.is_valid():

            customer_profile = customer_profile_serializer.save()


            address_data = request.data.get('address', {})
            address_data['customer'] = customer_profile.id  


            address_serializer = AddressSerializer(data=address_data)


            if address_serializer.is_valid():

                address_serializer.save()


                return Response({
                    "message": "Registration successful",
                    "customer_profile": customer_profile_serializer.data,
                    "address": address_serializer.data
                }, status=status.HTTP_201_CREATED)


            return Response({
                "message": "Error creating address",
                "errors": address_serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


        return Response({
            "message": "Error creating customer profile",
            "errors": customer_profile_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class UserProfileAPIView(APIView):
    def get(self, request, username):
        try:
            user = CustomerProfile.objects.get(username=username)
            serializer = CustomerProfileSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CustomerProfile.DoesNotExist:
            return Response({"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)


class UserLoginAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer = LoginSerializer(data=data)

        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')


            user = authenticate(request, email=email, password=password)

            if user is not None:

                refresh = RefreshToken.for_user(user)
                return Response({
                    "refresh_token": str(refresh),
                }, status=status.HTTP_200_OK)
            else:

                return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        else:

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

class LogoutView(APIView):
    def post(self, request):
        return Response(status=status.HTTP_204_NO_CONTENT)



