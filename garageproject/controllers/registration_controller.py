from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render
from django.conf import settings


def index(request):
    msg = ''
    return render(request, 'registration.html')