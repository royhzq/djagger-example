from rest_framework.views import APIView
from rest_framework.response import Response

from .schemas import (
    UserSchema,
    UserListSchema,
    LoginRequestSchema,
    LoginSuccessSchema,
    LoginErrorSchema,
    LogoutSuccessSchema
)

class CreateUserAPI(APIView):
    """This can only be done by the logged in user."""

    summary = "Create user"
    body_params = UserSchema
    response_schema = UserSchema

    def post(self, request):
        ...
        return Response({})

class CreateUsersListAPI(APIView):
    """ Creates list of users with given input array
    """
    summary = "Create array of Users"
    body_params = UserListSchema
    response_schema = UserListSchema

    def post(self, request):
        ...
        return Response({})

class Login(APIView):

    summary = "Logs user into the system"
    query_params = LoginRequestSchema
    response_schema = {
        "200":LoginSuccessSchema,
        "400":LoginErrorSchema
    }

    def get(self, request):
        ...
        return Response({})

class Logout(APIView):
    """ Logs current user session out of the system"""
    
    summary = "Logs out a User"
    response_schema = LogoutSuccessSchema

    def get(self, request):
        ...
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