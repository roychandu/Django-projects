from django.shortcuts import render
from .models import *

# Create your views here.
def indexpage(request):
    return render(request, "app/index.html")


def inserdata(request):
    fname_view = request.POST['fname_input']
    lname_view = request.POST['lname_input']
    email_view = request.POST['email_input']
    password_view = request.POST['password_input']

    newuser = singupdata.objects.create(first_name = fname_view, last_name = lname_view,
                                         email = email_view, password = password_view)
    
    return render(request, "app/show.html")