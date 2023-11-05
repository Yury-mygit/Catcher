from django.urls import path
from .controllers.api_controller import index, my_api, catch, request_handler
# from .test import index

urlpatterns = [
    path('', index),
    path('catch', catch, name='catch'),
    path('my-api/request/<uuid:requestId>', request_handler, name='request-handler'),
    path('my-api/', my_api, name='my-api'),
]

