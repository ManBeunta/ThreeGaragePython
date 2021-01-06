from django.shortcuts import render
from garageproject.models.brand_motor import Brand_motor
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    if request.method == 'POST':
        req = request.POST.dict()
        name = req['name']
        brand_motors = Brand_motor.objects.filter(name__contains=name)
    else:
        brand_motors = Brand_motor.objects.all()
    data = {
        'brand_motors': brand_motors
    }
    return render(request, 'brand/index.html', context=data)