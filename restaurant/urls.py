from django.urls import path, include
from restaurant import views

urlpatterns = [
    path('', views.index, name='index'),
]
