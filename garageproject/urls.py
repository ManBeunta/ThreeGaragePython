from django.urls import path
from garageproject.controllers import pemilik_controller, brand_controller, size_controller, registration_controller

urlpatterns = [
    path('', pemilik_controller.index, name='pemilik_index'),
    path('brand', brand_controller.index, name='brand_index'),
    path('size', size_controller.index, name='size_index'),
    path('register', registration_controller.index, name='register'),
]