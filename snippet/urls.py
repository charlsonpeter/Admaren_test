from rest_framework import routers
from django.conf.urls import url
from django.urls import path, include
from .views import *


router = routers.DefaultRouter()
router.register(r'snippet', SnippetLinkAPI)
router.register(r'tag', TagAPI)


urlpatterns = [
        path('', include(router.urls)),
        # path('snippet_api/', SnippetAPI.as_view(), name='snippet_api'),
    ]
