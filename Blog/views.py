from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response

from .schemas import (
    ArticleRequestSchema,
    ArticleDetailSchema,
    ArticleCreateSchema,
    ArticleDeleteSchema,
    ArticleYearSchema,
    ArticlePageSchema,
    ArticleHeaderSchema,
    ArticleCookieSchema,
    AuthorSchema,
    AuthorListSchema,
    AuthorIdSchema,
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

    body_params = ArticleCreateSchema
    response_schema = ArticleDetailSchema

    def post(self, request):
        ...
        return Response({})

class ArticleUpdateAPI(APIView):

    body_params = ArticleUpdateSerializer
    
    def put(self, request):
        ...
        return Response({})

class ArticleDeleteAPI(APIView):

    body_params = ArticleDeleteSchema

    def delete(self, request):
        ...
        return Response({})

class ArticlesYearAPI(APIView):
    """List all articles given a year"""

    path_params = ArticleYearSchema
    query_params = ArticlePageSchema
    header_params = ArticleHeaderSchema
    cookie_params = ArticleCookieSchema

    def get(self, request):
        ...
        return Response({})

@schema(
    methods=['GET', 'POST', 'DELETE'],
    summary="Authors API",
    post_body_params=AuthorSchema,
    delete_body_params=AuthorIdSchema,
    get_response_schema=AuthorListSchema,
    post_response_schema=AuthorSchema,
    delete_response_schema=AuthorIdSchema,
)
def author_api(request):
    """API to create an author, delete an author, or list all authors"""

    if request.method == 'get':
        ...

    if request.method == 'post':
        ...

    if request.method == 'delete':
        ...

class CategoryList(generics.ListCreateAPIView):
    """Example Generic View Documentation"""

    serializer_class = CategorySerializer(many=True)
    get_summary = "Category List"
    post_summary = "Category List Create"

    def list(self, request):
        ...

    def create(self, request):
        ...


class CategoryViewset(viewsets.ViewSet):
    """Example Viewset documentation"""
    
    response_schema = CategoryListSchema

    @schema(
        methods=['GET'],
        summary="List Categories",
    )
    def list(self, request):
        ...

    @schema(
        methods=['GET'],
        summary="Get Category",
        response_schema=CategorySerializer,
    )
    def retrieve(self, retrieve):
        ...