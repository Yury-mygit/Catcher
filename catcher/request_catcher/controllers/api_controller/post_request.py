from django.core.cache import cache
from django.http import JsonResponse
import json
from datetime import datetime
import uuid


def handler(request):
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
