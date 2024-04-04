from django.shortcuts import render
from .forms import MyForms
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = MyForms(request.POST)
        if form.is_valid():
            messages.success(request,("Your Request Submited!"))
        else:
            messages.success(request,("Invalid Captcha!"))
    form = MyForms()
    return render(request,"index.html",{'form':form})


def service(request):
    return render(request,"service-details.html",{})

def it_infra_service(request):
    return render(request,"it_infra_service.html",{})

def cloud_service(request):
    return render(request,"cloud_service.html",{})

def contact(request):
    return render(request, "contact.html",{})

def blog(request):
    return render(request, "blog.html",{})

def project(request):
    return render(request, "project.html",{})

def about(request):
    return render(request, "about.html",{})

