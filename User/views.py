from rest_framework.views import APIView
from rest_framework.response import Response

class CreateUserAPI(APIView):
    """ Create User
    """

    def post(self, request):
        return Response({})

class CreateUsersListAPI(APIView):
    """ Creates list of users with given input array
    """

    def post(self, request):
        return Response({})

class Login(APIView):
    """ Logs user into the system
    """
    def get(self, request):
        return Response({})

class Logout(APIView):
    """ Logs current user out of the system
    """
    def get(self, request):
        return Response({})

class User(APIView):
    """ Get a user by ``username``, update a user, or delete a user.
    """

    def get(self, request, username : str):
        return Response({})

    def put(self, request, username : str):
        return Response({})

    def delete(self, request, username : str):
        return Response({})