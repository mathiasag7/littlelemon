from rest_framework import serializers
from .models import Menu, Booking
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
        
        
class MenuSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Menu
        fields = ['id','title','price','inventory']


class BookingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Booking
        fields = '__all__'