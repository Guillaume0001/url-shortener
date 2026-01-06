from django.urls import path
from .views import *

urlpatterns = [
    path('<str:uid>', index),
    path('api/urls', list_urls),
    path('api/shorten/', create_url),
    path('api/url/<str:uid>', update_url),
    path('api/url/<str:uid>/delete', delete_url)
]