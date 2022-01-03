from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'cat', CategoryViewset, basename="cat")

urlpatterns = [
    path('articles/random', RandomArticleAPI.as_view()),
    path('articles/create', ArticleCreateAPI.as_view()),
    path('articles/update', ArticleUpdateAPI.as_view()),
    path('articles/delete/<int:pk>', ArticleDeleteAPI.as_view()),
    path('articles/<int:year>/', ArticlesYearAPI.as_view()),
    path('articles/<int:year>/<int:month>/<slug:slug>/', ArticleDetailAPI.as_view()),
    path('author', author_api),
    path('categories/', CategoryList.as_view()),
    path('', include(router.urls))
]

