from django.shortcuts import render

from .models import Job
# Create your views here.
def home(request):
    jobs = Job.objects #this gets all of your job objects from the database
    return render(request, 'jobs/home.html', {'jobs': jobs})

def test(request):
    return render(request, 'jobs/test.html')

def mail(request):
    return render(request, 'jobs/mail.php')


from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def newtest(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "jobs/newtest.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')