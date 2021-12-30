from rest_framework.views import APIView
from rest_framework.response import Response
from .schemas import (
    ToySchema, 
    ToyNotFoundSchema, 
    InvalidToySchema, 
    StatusSchema, 
    ToyArraySchema, 
    TagQueryParamSchema, 
    ToyIdSchema,
    ToyIdFormSchema,
    ToyDeleteHeaderSchema,
    ToyMetaDataSchema,
    ToyUploadImageSchema,
    ToyUploadImageSuccessSchema
)

class ToyAPI(APIView):
    """ Create a new Toy or update an existing Toy"""
    post_summary = "Add a new toy to the store"    
    post_body_params = ToySchema
    post_response_schema = ToySchema

    put_summary = "Update an existing toy"
    put_body_params = ToySchema
    put_response_schema = {
        "200":ToySchema,
        "400":InvalidToySchema,
        "404":ToyNotFoundSchema
    }

    def post(self, request):
        """Add a new Toy to the store"""
        ...
        return Response({})

    def put(self, request):
        """Update an existing Toy by Id"""
        ...
        return Response({})



class FindToyByStatusAPI(APIView):
    """ Find Toys by status"""

    summary = "Find Toys by status"
    query_params = StatusSchema
    response_schema = {
        "200":ToyArraySchema,
        "400":InvalidToySchema
    }

    def get(self, request):
        ...
        return Response({})


class FindToyByTagAPI(APIView):
    """Multiple tags can be provided with comma separated strings. e.g., ?tags=tag1,tag2"""

    summary = "Find Toys by tags"
    query_params = TagQueryParamSchema
    response_schema = {
        "200":ToyArraySchema,
        "400":InvalidToySchema
    }

    def get(self, request):
        ...
        return Response({})


class FindToyByIdAPI(APIView):

    get_summary = "Find Toy by ID"
    get_path_params = ToyIdSchema
    get_response_schema = {
        "200":ToySchema,
        "400":InvalidToySchema,
        "404":ToyNotFoundSchema
    }
    
    post_summary = "Update Toy with form data"
    post_body_params = {
        "multipart/form-data":ToyIdFormSchema
    }
    post_response_schema = {
        "405":InvalidToySchema
    }

    delete_summary = "Deletes a Toy"
    delete_header_params = ToyDeleteHeaderSchema
    delete_path_params = ToyIdSchema
    delete_response_schema = {
        "400":InvalidToySchema
    }

    def get(self, request, toyId: int):
        ...
        return Response({})

    def post(self, request, toyId: int):
        ...
        return Response({})

    def delete(self, request, toyId: int):
        ...
        return Response({})


class UploadImageAPI(APIView):

    summary = "Uploads an image"
    path_params = ToyIdSchema
    query_params = ToyMetaDataSchema
    body_params = {
        "application/octet-stream": ToyUploadImageSchema
    }
    response_schema = ToyUploadImageSuccessSchema

    def post(self, request, toyId: int):
        ...
        return Response({})
