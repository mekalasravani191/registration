from django.shortcuts import render,HttpResponse,redirect
from .models import EMP
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
# @login_required(login_url='login')
# def HomePage(request):
#     return render (request,'home.html')

@csrf_exempt
def SignupPage(request):
    if request.method=='POST': 
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        id = body['id']
        firstname = body['firstname']
        email = body['email']
        password = body['password']
        conform_password = body['conform_password']
        print(body,'-------------------------------------------------')
        print(id,firstname,email,password,conform_password,"------------")
        if password!=conform_password:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=EMP.objects.create(firstname=firstname,email=email,password=password,id=id,phone=123456789,lastname="test",gender="M")
            return HttpResponse("created")
            return redirect('login')
    
@csrf_exempt
def LoginPage(request):
    if request.method=='POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        email = body['email']
        password = body['password']
        users = getlist("email")
        
        if email in users:
            user_data=EMP.objects.get(email=email)
            if password==user_data.password:
                return HttpResponse('login successful')
            else:
                return HttpResponse('invalid password')
        else:
            return HttpResponse('user not found')
            
            
           

    # return render (request,'login.html')
def getlist(email):
    li = []
    alldata = EMP.objects.all()
    alldata = alldata.values()
    alldata = list(alldata)
    for single in alldata:
        li.append(single[email])
    return li
def LogoutPage(request):
    logout(request)
    return redirect('login')