from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response

from .schemas import (
    ArticleRequestSchema,
    ArticleDetailSchema,
    ListArticleDetailSchema,
    ArticleCreateSchema,
    ArticleDeleteSchema,
    ArticleYearSchema,
    ArticlePageSchema,
    ArticleHeaderSchema,
    ArticleCookieSchema,
    AuthorSchema,
    AuthorListSchema,
    CategoryListSchema,
)

from djagger.decorators import schema

from .serializers import ArticleUpdateSerializer, CategorySerializer

class RandomArticleAPI(APIView):
    """Return a random article from the Blog"""
    
    response_schema = ArticleDetailSchema

    def get(self, request):
        ...
        return Response({})

class ArticleDetailAPI(APIView):

    path_params = ArticleRequestSchema
    response_schema = ArticleDetailSchema

    def get(self, request):
        ...
        return Response({})


class ArticleCreateAPI(APIView):

    request_schema = ArticleCreateSchema
    response_schema = ArticleDetailSchema

    def post(self, request):
        ...
        return Response({})

class ArticleUpdateAPI(APIView):

    request_schema = ArticleUpdateSerializer
    response_schema = ArticleDetailSchema
    
    def put(self, request):
        ...
        return Response({})

class ArticleDeleteAPI(APIView):

    path_params = ArticleDeleteSchema
    response_schema = ArticleDeleteSchema

    def delete(self, request):
        ...
        return Response({})

class ArticlesYearAPI(APIView):
    """List all articles given a year"""

    path_params = ArticleYearSchema
    query_params = ArticlePageSchema
    header_params = ArticleHeaderSchema
    cookie_params = ArticleCookieSchema
    response_schema = ListArticleDetailSchema

    def get(self, request):
        ...
        return Response({})

@schema(
    methods=['GET', 'POST'],
    get_summary="List Authors",
    get_response_schema=AuthorListSchema,
    post_summary="Create Author",
    post_request_schema=AuthorSchema,
    post_response_schema=AuthorSchema,
)
def author_api(request):
    """API to create an author or list all authors"""

    if request.method == 'get':
        ...
        return Response({})

    if request.method == 'post':
        ...
        return Response({})

class CategoryList(generics.ListCreateAPIView):
    """Example Generic View Documentation"""

    serializer_class = CategorySerializer(many=True)
    get_summary = "Category List"
    post_summary = "Category List Create"

    def list(self, request):
        ...
        return Response({})

    def create(self, request):
        ...
        return Response({})

class CategoryViewset(viewsets.ViewSet):
    """Example Viewset documentation"""
    
    response_schema = CategoryListSchema

    @schema(
        methods=['GET'],
        summary="List Categories",
    )
    def list(self, request):
        ...
        return Response({})

    @schema(
        methods=['GET'],
        summary="Get Category",
        response_schema=CategorySerializer,
    )
    def retrieve(self, retrieve):
        ...
        return Response({})