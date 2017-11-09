from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render
from eliveapp.models import Channel
import logging
from django.contrib.auth.decorators import login_required
from eliveapp.hashutils import HashUtils

def register(request):
    return render(request, 'registration/register.html')
