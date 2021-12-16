from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import OrderSerializer
from .schemas import Toy
class InventoryAPI(APIView):
    """ Returns toy inventories by status
    """

    def get(self, request):
        return Response({})

class PlaceOrderAPI(APIView):
    """ Place an order for a toy
    """
    consumes = ["application/xml"]
    get_consumes = ["application/xml"]
    get_path_params = Toy
    post_response_schema = Toy
    put_response_schema = Toy

    def post(self, request):
        return Response({})

    def put(self, request):
        return Response({})


class OrderAPI(APIView):
    """ Find an order or delete and order by Id
    """

    def get(self, request, orderId : int):
        return Response({})

    def delete(self, request, orderId : int):
        return Response({})


from rest_framework import viewsets
class OrderViewSet(viewsets.GenericViewSet):
    """ Test order Generic viewset
    """

    serializer_class = OrderSerializer

    def list(self, request):
        queryset=[]
        return Response({})

    def retrieve(self, request):
        queryset=[]
        return Response({})

