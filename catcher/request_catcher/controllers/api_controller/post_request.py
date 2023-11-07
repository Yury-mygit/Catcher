from django.core.cache import cache
from django.http import JsonResponse
import json
from datetime import datetime
import uuid
import pickle


def handler(request):
    print(type(request.body.decode('utf-8')))
    request_body = request.body.decode('utf-8')
    request_headers = dict(request.headers)
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
    request_details = {
        'id': str(uuid.uuid4()),
        'URL': request.build_absolute_uri(),
        'Network': network_details,
        'Request_Headers': request_headers,
        'Request_Body': json.loads(request_body) if request_body else {},
        'Datetime': f"Date: {formatted_date}. Time: {formatted_time}",
        'status': 'active'
    }
    request_details_json = json.dumps(request_details)
    existing_data = cache.get('request_key')
    if existing_data is None:
        existing_data = []
    existing_data.append(request_details_json)
    cache.set('request_key', existing_data)
    # print(existing_data)
    return JsonResponse(existing_data, safe=False)


