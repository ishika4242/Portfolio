from django.shortcuts import render,redirect
from .models import Workings, Servicing, Contacting
from website.models import Contacting
from django.contrib import messages
# Create your views here.
def index(request):

    works = Workings.objects.all()
    services = Servicing.objects.all()

    
    return render(request,"index.html",{'works':works,'services':services})

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']     
        contact = Contacting(name = name,email = email, subject = subject,message = message)
        contact.save()
        return redirect('/')

    else:
        return render(request,"index.html")

