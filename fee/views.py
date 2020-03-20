from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from .models import Resident
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'fee/index.html')


def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')   
        phone = request.POST.get('phone')
        temp_isOwner = request.POST.get('isOwner')
        if temp_isOwner != 'True':
            isOwner = False
        else:
            isOwner = True
        temp_multipleFlats = request.POST.get('multipleFlats')
        flatNo1 = request.POST.get('flatNo1')
        if temp_multipleFlats != 'True':
            multipleFlats = False
        else:
            multipleFlats = True
            flatNo2 = '0'
        flatNo2 = request.POST.get('flatNo2')
        #print(isOwner, multipleFlats)
        user = User.objects.create_user(username=username, password=password)
        resident = Resident(user=user, email=email, firstname=firstname, lastname=lastname, phone=phone, isOwner=isOwner, multipleFlats=multipleFlats, flatNo1=flatNo1, flatNo2=flatNo2)
        resident.save()
        return render(request, 'fee/login.html')
    elif request.method == 'GET':
        return render(request, 'fee/signup.html')


def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'fee/success.html')
        else:
            messages.error(request, 'Invalid Credentials!')
    return render(request, 'fee/login.html')


def check_username(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        data = {
            "is_taken" : User.objects.filter(username__iexact=username).exists()
        }
        if data["is_taken"]:
            data["error_message"] = "This username is already taken!"
        else:
            data["success_message"] = "Username available!"
        return JsonResponse(data)
    else:
        return JsonResponse({"request_error" : 'Something went wrong!'})