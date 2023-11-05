from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from django.shortcuts import render, get_object_or_404
import json
from datetime import datetime
from django.urls import reverse

import uuid

def index(request):
    return HttpResponse("<h4>Проверка работы!!</h4>")


@csrf_exempt
def catch(request):
    # Get the serialized request data from Redis
    raw_request_data_json_list = cache.get('request_key')

    # Check if raw_request_data_json_list is None
    if raw_request_data_json_list is None:
        # Render the welcome.html template for the welcome page
        return render(request, 'request_catcher/welcome.html', {'api_url': reverse('my-api')})
    else:
        # Deserialize each JSON string in the list
        request_data = [json.loads(raw_request_data_json) for raw_request_data_json in raw_request_data_json_list]

        # print(request_data)
        # Filter the request data for active requests
        active_requests = [data for data in request_data if data['status'] == 'active']

        # Check if there are any active requests
        if active_requests:
            # If there are active requests, render the 'catch' template
            return render(request, 'request_catcher/catch.html', {'request_data': request_data, 'api_url': reverse('my-api')})
        else:
            # If there are no active requests, render the 'welcome' template
            return render(request, 'request_catcher/welcome.html', {'api_url': reverse('my-api')})


@csrf_exempt
def catch_all(request):
    # This view will catch all types of requests
    return JsonResponse({'message': 'Request received'})


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
                # Mark the request as inactive

                request_data['status'] = 'inactive'

                # Update the request data in the existing data list

                existing_data[i] = json.dumps(request_data)

                # Update the request data in Redis

                cache.set('request_key', existing_data)

                return JsonResponse({'message': 'Request marked as inactive'})

        # Return a 404 response if the request ID is not found

        return JsonResponse({'status': 'error', 'message': 'Request ID not found'}, status=404)

@csrf_exempt
def my_api(request):
    if request.method == 'GET':
        # Handle GET request
        return JsonResponse({'message': 'This is a GET request'})
    elif request.method == 'POST':
        # Get the request body as text
        request_body = request.body.decode('utf-8')

        # Get the request headers
        request_headers = dict(request.headers)

        # Get the network details
        network_details = {
            'local': {
                'address': request.META['REMOTE_ADDR'],
                'family': 'IPv4',
                'port': request.META['SERVER_PORT']
            },
            'remote': {
                'address': request.META['REMOTE_HOST'] if 'REMOTE_HOST' in request.META else 'Unknown',
                'family': 'IPv4',
                'port': request.META['REMOTE_PORT'] if 'REMOTE_PORT' in request.META else 'Unknown'
            }
        }

        now = datetime.now()
        formatted_date = now.strftime("%A, %d %B %Y")
        formatted_time = now.strftime("%H:%M:%S")


        # Prepare the request details
        request_details = {
            'id': str(uuid.uuid4()),
            'URL': request.build_absolute_uri(),
            'Network': network_details,
            'Request_Headers': request_headers,
            'Request_Body': json.loads(request_body) if request_body else {},
            'Datetime': f"Date: {formatted_date}. Time: {formatted_time}",
            'status': 'active'  # Add this line
        }

        # print(request_details)
        # Serialize the request details to a JSON-formatted string
        request_details_json = json.dumps(request_details)

        # Get the existing request data from Redis
        existing_data = cache.get('request_key')

        # If there's no existing data, create a new list
        if existing_data is None:
            existing_data = []

        # Append the new request data to the existing data
        existing_data.append(request_details_json)

        # Store the updated request data in Redis
        cache.set('request_key', existing_data)

        return JsonResponse({'message': 'POST request received and stored in Redis'})
    else:
        # Handle other types of requests
        return JsonResponse({'message': 'This is neither a GET nor a POST request'})
