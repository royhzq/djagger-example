from django.urls import path, include
from .views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'order_sets', OrderViewSet, basename='MyOrders')

urlpatterns = [
    path('inventory', InventoryAPI.as_view()),
    path('order', PlaceOrderAPI.as_view()),
    path('order/<int:orderId>', OrderAPI.as_view()),
    path("", include(router.urls))
]
