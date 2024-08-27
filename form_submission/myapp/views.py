from django.shortcuts import render
from .models import*

# Create your views here.
def showindex(request):
    return render(request, "app/index.html")


def InserData(request):
    fname_view = request.POST['fname_input']
    lname_view = request.POST['lname_input']
    email_view = request.POST['email_input']
    phone_view = request.POST['phone_input']
    address1_view = request.POST['address_input']
    address2_view = request.POST['address2_input']
    state_view = request.POST['state_input']
    country_view = request.POST['country_input']
    post_view = request.POST['post_input']
    area_view = request.POST['area_input']

    newUser = FormData.objects.create(first_name = fname_view, last_name = lname_view,
                                      email = email_view, contact = phone_view, address1_field = address1_view, address2_field = address2_view, state_field = state_view, country_field = country_view, post_field = post_view, area_field = area_view)
    
    return render(request, "app/show.html")