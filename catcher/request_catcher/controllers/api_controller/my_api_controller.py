from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


from .post_request import handler as post_handler

@csrf_exempt
def my_api(request):
    if request.method == 'GET':
        # Handle GET request
        return JsonResponse({'message': 'This is a GET request'})
    elif request.method == 'POST':
        # Get the request body as text
        return post_handler(request)
    else:
        # Handle other types of requests
        return JsonResponse({'message': 'method is not supported'})