from django.shortcuts import render
from garageproject.models.brand_motor import Brand_motor

def index(request):
    brand_motors = Brand_motor.objects.all()
    data = {
        'brand_motors': brand_motors
    }
    return render(request, 'brand/index.html', context=data)