from django.http import HttpResponse
from django.shortcuts import render
from .models import Job
from django.utils.text import Truncator

def index(request):
    jobs = ""
    if request.user.is_authenticated():
        current_user = request.user
        jobs = Job.objects.filter(user=current_user).order_by('-date')
    return render (request, 'index.html', {'jobs':jobs})
