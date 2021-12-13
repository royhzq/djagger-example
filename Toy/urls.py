from django.urls import path
from .views import *

urlpatterns = [
    path('', ToyAPI.as_view()),
    path('findByStatus', FindToyByStatusAPI.as_view()),
    path('findByTags', FindToyByTagAPI.as_view()),
    path('<int:toyId>', FindToyByIdAPI.as_view()),
    path('<int:toyId>/uploadImage', UploadImageAPI.as_view()),
]
