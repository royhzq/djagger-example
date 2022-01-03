from rest_framework.views import APIView
from rest_framework.response import Response

from .schemas import (
    UserSchema,
    UserListSchema,
    UsernameSchema,
    UserErrorSchema,
    LoginRequestSchema,
    LoginSuccessSchema,
    LoginErrorSchema,
    ForbiddenSchema,
    LogoutSuccessSchema
)

class CreateUserAPI(APIView):
    """This can only be done by the logged in user."""

    summary = "Create user"
    request_schema = UserSchema
    response_schema = UserSchema

    def post(self, request):
        ...
        return Response({})

class CreateUsersListAPI(APIView):
    """ Creates list of users with given input array"""

    summary = "Create array of Users"
    request_schema = UserListSchema
    response_schema = UserListSchema

    def post(self, request):
        ...
        return Response({})

class Login(APIView):

    summary = "Logs user into the system"
    query_params = LoginRequestSchema
    response_schema = {
        "200":LoginSuccessSchema,
        "400":LoginErrorSchema,
        ("403", "text/plain"): ForbiddenSchema
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

    get_summary = "Get User"
    put_summary = "Update User"
    delete_summary = "Delete User"

    path_params = UsernameSchema
    response_schema = {
        '200':UserSchema,
        '400':UserErrorSchema,
        '404':UserErrorSchema
    }
    delete_response_schema = {
        '400':UserErrorSchema,
        '404':UserErrorSchema
    }

    def get(self, request, username : str):
        """Retrieve a User by username"""
        ...
        return Response({})

    def put(self, request, username : str):
        """Update a User by username"""
        ...
        return Response({})

    def delete(self, request, username : str):
        """Delete a User by username"""
        ...
        return Response({})