from django.shortcuts import render,redirect
from app6.models import mytable
from django.http import HttpResponse
from django.contrib.auth import authenticate, login,logout

def register(request):
    if request.method=="POST":
        Name=request.POST["name1"]
        Age= request.POST["name2"]
        Email= request.POST["name3"]
        Phoneno= request.POST["name4"]
        Dob= request.POST["name5"]
        Username= request.POST["name6"]
        Password= request.POST["name7"]

        db=mytable(Name=Name,Age=Age,Email=Email,Phoneno=Phoneno,Dob=Dob,Username=Username,Password=Password)
        db.save()

        return HttpResponse("data saved")


    return render(request,"register.html")

def signin(request):
    if request.method == "POST":
        a= request.POST["name1"]
        b= request.POST["name2"]
        try:
            q=mytable.objects.get(Username=a)


        except mytable.DoesNotExist:
            return HttpResponse("Incorrect Password/Username")

        if q.Password==b:
            request.session["member_id"]=q.id
            return render(request,"welcome.html")
        else:
            return HttpResponse("incorrect username/password")
    return render(request, "signin.html")




def run(request):
    return render(request,"home.html")


def welcome(request):
    return render(request,"welcome.html")
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('welcome')
        else:
            return HttpResponse("Invalid credentials")
    return render(request, 'new_login.html')

def userdata(request):
    a=mytable.objects.get(id=request.session["member_id"])
    return render(request,"userdata.html",{"key5":a})

def lod(request):
    logout(request)
    return  redirect("run")