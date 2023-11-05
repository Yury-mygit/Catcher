from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from django.http import JsonResponse
import json


@csrf_exempt
def request_handler(request, requestId=None):
    if request.method == 'GET':
        print('dsdssddssssssssssssssssssssssssssssssssssssssssssssssssss')
        return JsonResponse({'message': 'Wrong request'})

    elif request.method == 'POST':
        pass

    elif request.method == 'PUT':
        pass


    elif request.method == 'DELETE':
        print('DELETE running')
        # Get the existing request data from Redis
        existing_data = cache.get('request_key')
        if existing_data is not None:
            # Find the request data with the matching ID
            request_data = None
            for i, data in enumerate(existing_data):
                data_dict = json.loads(data)

                print(str(data_dict['id']))

                if str(data_dict['id']) == str(requestId):  # Compare requestId directly
                    request_data = data_dict
                    break
            if request_data is not None:
                # Remove the request data from the existing data list
                existing_data.remove(json.dumps(request_data))
                # Update the request data in Redis
                cache.set('request_key', existing_data)
                return JsonResponse({'message': 'Request deleted successfully'})
        # Return a 404 response if the request ID is not found
        return JsonResponse({'status': 'error', 'message': 'Request ID not found'}, status=404)


