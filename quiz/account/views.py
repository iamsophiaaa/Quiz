from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
# Create your views here.
def register(request):
    if request.method =='GET':
        return render(request, "register.html" )
    if request.method == 'POST':
        uname= request.POST.get('username')
        email= request.POST.get('email')
        pass1= request.POST.get('password1')
        pass2= request.POST.get('password2')
        if(pass1 != pass2):
            pass
        else:
            new_user = User.objects.create_user(uname, email, pass1)
            new_user.save()
            return redirect('login')

    
    

def login(request):
    if request.method=='GET':
        context={}
        return render(request ,"login.html", context )
    if request.method == 'POST':
        error = ''
        uname = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=uname, password=password)
        if user:
            login(request, user)
            return redirect('catalogue:dashboard')
        error='credentials do not match'
        return render(request ,"login.html", {'error':error} )
    
def user_logout(request):
    logout(request)
    return redirect('catalogue:dashboard')