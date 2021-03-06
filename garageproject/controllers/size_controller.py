from django.shortcuts import render
from garageproject.models.size_motor import Size_motor
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    size_motors = Size_motor.objects.all()
    data = {
        'size_motors': size_motors
    }
    return render(request, 'size/index.html', context=data)