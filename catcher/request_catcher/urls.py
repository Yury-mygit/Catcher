from django.urls import path

from .controllers.api_controller.get_all import get_all_requests
# from .controllers.api_controller import index, my_api, catch, request_handler
from .controllers.main_view_controller import index
from .controllers.catch_controller import catch
from .controllers.request_handler_controller import request_handler
from .controllers.api_controller.my_api_controller import my_api
# from .test import index

urlpatterns = [
    path('', index),
    path('catch', catch, name='catch'),
    path('my-api/request/<uuid:requestId>', request_handler, name='request-handler'),
    path('my-api/', my_api, name='my-api'),
    path('get_all_requests/', get_all_requests, name='get_all_requests'),
]

