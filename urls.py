from django.urls import path, include
from . import views
app_name="tabularosa"

urlpatterns = [
    path('map/', views.world_map, name='map'),
   
]
