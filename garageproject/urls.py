from django.urls import path
from garageproject.controllers import pemilik_controller, brand_controller


urlpatterns = [
    path('', pemilik_controller.index, name='pemilik_index'),
    path('brand', brand_controller.index, name='brand_index'),
]