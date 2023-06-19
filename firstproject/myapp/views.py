import email
from django.shortcuts import render
from django.db import connection
from .models import Student
#from django.core.validators import validate_email
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.
def home(request):
    x=11
    info=[1,2,3,4,5,6,7,8,9,10]
    name=['A','B','C','D','E','F','G','H','I','J']
    allinfo=[{'name':name[i],'info':info[i]} for i in range (len(info))]
    print(allinfo)
    vars={'allinfo':allinfo}
    return render(request,'home.html',vars)

"""def new (request):
    cursor=connection.cursor()
    sql="SELECT * FROM myapp_student;"
    cursor.execute(sql)
    result=cursor.fetchall()
    print(result)"""
def new(request):
    result=Student.objects.all()
    for results in result:
        print(results.name,results.age)
    return render(request,'new.html')


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        if password == password2:
            if User.objects.filter(username=username).exists():
                return HttpResponse ("Username already exists")
            elif User.objects.filter(email=email).exists(): 
                return HttpResponse("email already exists")
            else:
                try:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=lastname)
                    user.save()
                    return HttpResponse("User created Successfuly")
                except:
                    return HttpResponse("Error")
        else:
            return HttpResponse("PASSWORDS DO NOT MATCH")


    else:
        return render(request,'userauth/signup.html')
    

def signing(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return HttpResponse("Login Succesful")
        else:
            return HttpResponse("Loging Fail,wrong username and password")
    return render(request,"userauth/loging.html")