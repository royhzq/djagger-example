from rest_framework.views import APIView
from rest_framework.response import Response
from .schemas import Toy


class ToyAPI(APIView):
    """ Create a new Toy or update an existing Toy
    """
    
    summary = "Add a new toy to the store"
    consumes = ["application/json", "application/xml"]
    produces = ["application/json", "application/xml"]
    
    post_response_schema = Toy
    put_response_schema = Toy

    def get(self, request):
        return Response({})

    def post(self, request):
        return Response({})

    def put(self, request):
        return Response({})



class FindToyByStatusAPI(APIView):
    """ Find Toys by status
    """

    def get(self, request):
        return Response({})


class FindToyByTagAPI(APIView):
    """ Find Toys by tags
    """

    def get(self, request):
        return Response({})


class FindToyByIdAPI(APIView):
    """ Find Toys by Id
    """

    def get(self, request, toyId: int):
        return Response({})

    def post(self, request, toyId: int):
        return Response({})

    def delete(self, request, toyId: int):
        return Response({})


class UploadImageAPI(APIView):
    """ Uploads an image
    """

    def post(self, request, toyId: int):
        return Response({})
