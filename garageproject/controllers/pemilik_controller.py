from django.shortcuts import render
from garageproject.models.pemilik_motor import Pemilik_motor
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    if request.method == 'POST':
        req = request.POST.dict()
        name = req['name']
        pemilik_motors = Pemilik_motor.objects.filter(name__contains=name)
    else:
        pemilik_motors = Pemilik_motor.objects.all()
    data = {
        'pemilik_motors': pemilik_motors
    }
    return render(request, 'owner/index.html', context=data)