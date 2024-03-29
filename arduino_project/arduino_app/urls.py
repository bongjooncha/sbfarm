from django.urls import path
from . import views

urlpatterns = [
    path('getWaterLevel/', views.get_water_level_view, name='get_water_level'),
    # 다른 URL 매핑들...
]
