from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from django.urls import reverse
import json


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
            return render(request, 'request_catcher/catch.html',
                          {'request_data': request_data, 'api_url': reverse('my-api')})
        else:
            # If there are no active requests, render the 'welcome' template
            return render(request, 'request_catcher/welcome.html', {'api_url': reverse('my-api')})
