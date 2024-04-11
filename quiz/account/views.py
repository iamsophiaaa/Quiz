from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout, login
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

    
    

def login_user(request):
    if request.method=='GET':
        
        return render(request ,"login.html" )
    if request.method == 'POST':
        error = ''
        uname = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=uname, password=password)
        if user is not None:
            login(request, user)
            return redirect('catalogue:dashboard')
        
        else:
            error='Credentials do not match'
            print(error)
            return render(request ,"login.html", {'error':error} )
    
def logout_user(request):
    logout(request)
    return redirect('catalogue:dashboard')