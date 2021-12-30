from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OrderSerializer
from .schemas import (
    InventoryByStatusSchema,
    OrderSchema,
    OrderIDSchema,
    InvalidInputSchema,
    NotFoundSchema,

)

class InventoryAPI(APIView):

    summary = "Returns toy inventories by status"
    response_schema = InventoryByStatusSchema

    def get(self, request):
        ...
        return Response({})


class PlaceOrderAPI(APIView):

    summary = "Place an order for a toy"
    body_params = OrderSchema
    response_schema = {
        "200" : OrderSchema,
        "405" : InvalidInputSchema
    }

    def post(self, request):
        ...
        return Response({})


class OrderAPI(APIView):

    get_summary = "Find purchase order by ID"
    path_params = OrderIDSchema 
    get_response_schema = {
        "200" : OrderSchema,
        "404" : NotFoundSchema,
        "400" : InvalidInputSchema
    }

    delete_summary = "Delete purchase order by ID"
    delete_response_schema = {
        "404" : NotFoundSchema,
        "400" : InvalidInputSchema
    }

    def get(self, request, orderId : int):
        ...
        return Response({})

    def delete(self, request, orderId : int):
        ...
        return Response({})