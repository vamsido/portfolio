from django.shortcuts import render

from .models import job
# Create your views here.


def home(request):
    newjobs = job.objects.all()
    return render(request,"jobs/home.html",{"jobs":newjobs})
