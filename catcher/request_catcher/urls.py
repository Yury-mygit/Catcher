from django.urls import path
from .views import catch_all, index, my_api, catch, request_handler
import uuid

urlpatterns = [
    path('', index),
    path('catch', catch, name='catch'),
    # path('my-api/', my_api)
    # path('my-api/request/${requestId}', request_handler, name='my-api'),
    path('my-api/request/<uuid:requestId>', request_handler, name='request-handler'),
    path('my-api/', my_api, name='my-api'),
]

