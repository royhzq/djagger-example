from rest_framework.views import APIView
from rest_framework.response import Response

class InventoryAPI(APIView):
    """ Returns toy inventories by status
    """

    def get(self, request):
        return Response({})

class PlaceOrderAPI(APIView):
    """ Place an order for a toy
    """

    def post(self, request):
        return Response({})

class OrderAPI(APIView):
    """ Find an order or delete and order by Id
    """

    def get(self, request, orderId : int):
        return Response({})

    def delete(self, request, orderId : int):
        return Response({})
