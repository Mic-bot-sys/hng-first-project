from django.http import JsonResponse
from django.shortcuts import render
import logging
from services.helper import get_client_ip, get_location

logger = logging.getLogger("locator_app.views") 


# Create your views here.
def welcome(request):
    try:
        visitor_name = request.GET.get('visitor_name', 'Guest')
        client_ip = get_client_ip(request)
        location, temperature = get_location(client_ip).values()
        greeting = f'Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {location}'
        return JsonResponse({
            'client_ip': client_ip,
            'location': location,
            'greeting': greeting
        })
    except Exception as ex:
        logger.exception("An error occured while getting the location and temperature details.")
        return JsonResponse({"message": "An Error Occured in the Server", "status": "500"})
