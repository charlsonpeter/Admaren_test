from django.conf.urls import url
from django.urls import path
from .views import *



urlpatterns = [
        path('register/', RegisterApi.as_view()),
        path('login/', UserLogin.as_view()),
        path('refresh/', RefreshToken.as_view()),
        path('logout/', logout_user, name='logout'),
    ]
