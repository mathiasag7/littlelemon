from django.urls import path, include
from restaurant import views

urlpatterns = [
    path('items/', views.MenuItemsView.as_view()),
    path('items/<int:pk>', views.SingleMenuItemView.as_view()),
]
