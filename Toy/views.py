from rest_framework.views import APIView
from rest_framework.response import Response


class ToyAPI(APIView):
    """ Create a new Toy or update an existing Toy
    """

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
