from django.shortcuts import render
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User
from .serializers import UserSerializer
# Create your views here.

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated]


class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    