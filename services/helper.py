# import requests
from django.http import JsonResponse
import requests
from decouple import config

api_key = config("API_KEY", default="")
req_url = f"{config("BASE_URL", default="")}?key={api_key}&"

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



def get_location(ip="Lagos"):
    response = requests.get(f'{req_url}q={ip}')
    data = response.json()
    location = data["location"]["name"]
    temperature = data["current"]["temp_c"]
    return {"location": location, "temperature": temperature}
