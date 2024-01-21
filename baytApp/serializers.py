from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserRegistrationSerializer (serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    username = serializers.CharField()
    email = serializers.CharField()
    class Meta:
        model = User        
        fields =fields = '__all__'        

    def create(self, validated_data):
        user_data = { 
            'first_name': validated_data['first_name'],
            
            'username': validated_data['username'],         
            'email': validated_data['email'],
            'password': validated_data['password'],
        }
              
        return User.objects.create_user(**user_data)
    
class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ['id', 'username', 'email', 'first_name',]

class PremiumJobSerializer (serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'

class JobSerializer (serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['name', 'industry', 'region', 'country', 'salary']