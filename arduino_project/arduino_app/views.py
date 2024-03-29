from django.http import JsonResponse
from .serial_helper import get_water_level

def get_water_level_view(request):
    water_level = get_water_level()
    return JsonResponse({'water_level': water_level})
