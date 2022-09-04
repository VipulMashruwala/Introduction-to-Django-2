import imp
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.db import connection
from django.db.models import Q
from .models import MyUser, MyAdmin
from django.core.exceptions import *


# Create your views here.
# def index(request):
#     return render(request, 'templates/index.html')

def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def index(request):
    return render(request, 'index.html')

def check_credentials(request):
    adminname = request.POST.get('user_name')
    password = request.POST.get('password')

    try:
        obj2 = MyAdmin.objects.get(admin_name = adminname, admin_password = password)
    except MyAdmin.DoesNotExist:
        return HttpResponse('<script> alert("Invalid User");  window.location.replace("/auth"); </script>')
    return showData(request,"Login Successfully")

def showData(request,message):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM awesome_auth_myuser")
    r = dictfetchall(cursor)

    if len(r) != 0:
        msg = message
    else:
        msg = None
    return render(request,'home.html',{'data': r, 'message' : msg})

def addNewAdmin(request):
    adminname = request.POST.get('user_name')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')
    if password == confirm_password and len(adminname) != 0:
        try:
            obj = MyAdmin.objects.get(admin_name = adminname)
        except MyAdmin.DoesNotExist:
            obj1 = MyAdmin(admin_name= adminname, admin_password = password)
            obj1.save()
            return render(request,'index.html')
        return HttpResponse('<script> alert("User Already Exist");</script>')
    else:
        return HttpResponse('<script> alert("Invalid Input");</script>')

def addData(request):
    username = request.POST.get('user_name')
    address = request.POST.get('user_address')
    phone = request.POST.get('user_phone')
    obj1 = MyUser(user_name=username, user_address = address, user_phone = phone)
    obj1.save()
    return showData(request,"Data Added Successfully")

def updateData(request):
    userid = request.POST.get('user_id')
    username = request.POST.get('user_name')
    address = request.POST.get('user_address')
    phone = request.POST.get('user_phone')

    obj2 = MyUser.objects.get(user_id = userid)

    if username != "":    
        obj2.user_name = username
        obj2.save()
    
    if address != "":
        obj2.user_address = address
        obj2.save()

    if phone != "":
        obj2.user_phone = phone
        obj2.save()
    return showData(request,"Data Updated Successfully")

def deleteData(request):
    userid = request.POST.get('user_id')
    obj3 = MyUser.objects.get(user_id = userid)
    obj3.delete()

    return showData(request,"Data Deleted Successfully")

def signup(request):
    return render(request,'signup.html')



