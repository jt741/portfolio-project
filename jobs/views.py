from django.shortcuts import render

from .models import Job
# Create your views here.
def home(request):
    jobs = Job.objects #this gets all of your job objects from the database
    return render(request, 'jobs/home.html', {'jobs': jobs})

def test(request):
    return render(request, 'jobs/test.html')