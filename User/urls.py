from django.urls import path
from .views import *

urlpatterns = [
    path('', CreateUserAPI.as_view()),
    path('createWithList', CreateUsersListAPI.as_view()),
	path('login', Login.as_view()),
	path('logout', Logout.as_view()),
	path('<str:username>', User.as_view())	  
]
