from django.shortcuts import render
from .models import con_dtls

# Create your views here.


def About(request):

    context = {}

    return render(request,'con_dtails/about.html',context)


def contact(request):


    if request.method == "POST":
        name = request.POST['cName']
        email = request.POST['cEmail']
        site = request.POST['cWebsite']
        msg = request.POST['cMessage']
        data = con_dtls(
            name = name,
            email = email,
            site = site,
            msg = msg,
        )
        data.save()
        context = {'data':data}

    context = {}

    return render(request,'con_dtails/contact.html',context)

def term(request):

    return render(request,'con_dtails/Terms.html')

def privacy(request):

    return render(request,'con_dtails/privacy_policy.html')