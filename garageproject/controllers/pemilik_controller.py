from django.shortcuts import render
from garageproject.models.pemilik_motor import Pemilik_motor

def index(request):
    pemilik_motors = Pemilik_motor.objects.all()
    data = {
        'pemilik_motors': pemilik_motors
    }
    return render(request, 'owner/index.html', context=data)