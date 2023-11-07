from django.core.cache import cache
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def get_all_requests(request):
    if request.method == 'GET':
        data = cache.get('request_key', [])
        # Deserialize the data if it's not an empty list
        if data:
            data = [json.loads(item) for item in data]
        return JsonResponse(data, safe=False)
    else:
        return HttpResponseNotAllowed(['GET'], json.dumps({"error": "Method not allowed"}))



# [
#     {
#         "id": "8dde061a-717e-408d-bb31-09509545da8f",
#         "URL": "http://127.0.0.1:802/my-api/",
#         "Network": {
#             "local": {
#                 "address": "172.18.0.1",
#                 "family": "IPv4",
#                 "port": "80"
#             },
#             "remote": {
#                 "address": "",
#                 "family": "IPv4",
#                 "port": "Unknown"
#             }
#         },
#         "Request_Headers": {
#             "Content-Length": "831",
#             "Content-Type": "application/json",
#             "User-Agent": "PostmanRuntime/7.34.0",
#             "Accept": "*/*",
#             "Cache-Control": "no-cache",
#             "Postman-Token": "a99c3b3a-f7ec-4a7c-8f84-c360cf69ef7e",
#             "Host": "127.0.0.1:802",
#             "Accept-Encoding": "gzip, deflate, br",
#             "Connection": "keep-alive"
#         },
#         "Request_Body": {
#             "squadName": "Super hero squad",
#             "homeTown": "Metro City",
#             "formed": 2016,
#             "secretBase": "Super tower",
#             "active": true,
#             "members": [
#                 {
#                     "name": "Molecule Man",
#                     "age": 29,
#                     "secretIdentity": "Dan Jukes",
#                     "powers": [
#                         "Radiation resistance",
#                         "Turning tiny",
#                         "Radiation blast"
#                     ]
#                 },
#                 {
#                     "name": "Madame Uppercut",
#                     "age": 39,
#                     "secretIdentity": "Jane Wilson",
#                     "powers": [
#                         "Million tonne punch",
#                         "Damage resistance",
#                         "Superhuman reflexes"
#                     ]
#                 },
#                 {
#                     "name": "Eternal Flame",
#                     "age": 1000000,
#                     "secretIdentity": "Unknown",
#                     "powers": [
#                         "Immortality",
#                         "Heat Immunity",
#                         "Inferno",
#                         "Teleportation",
#                         "Interdimensional travel"
#                     ]
#                 }
#             ]
#         },
#         "Datetime": "Date: Monday, 06 November 2023. Time: 21:52:05",
#         "status": "active"
#     }
# ]