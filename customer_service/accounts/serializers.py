from rest_framework import serializers
from .models import CustomerProfile, Address



class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class CustomerProfileSerializer(serializers.ModelSerializer):


    class Meta:
        model = CustomerProfile
        fields = '__all__'


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128)