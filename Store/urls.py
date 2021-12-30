from django.urls import path, include
from .views import *

urlpatterns = [
    path('inventory', InventoryAPI.as_view()),
    path('order', PlaceOrderAPI.as_view()),
    path('order/<int:orderId>', OrderAPI.as_view()),
]
