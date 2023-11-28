from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from customer.forms import UserRegisterForm

# Create your views here.
def login_user(request):
    try:
        if request.method == 'POST':
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Main_page')
            else:
                messages.success(request, ('There was an error Occured!!!'))
                return redirect('login')
        else:    
            return render(request, 'login.html', {})
    except:
        messages.error(request, "Login Url Page Error Occurred")
    

def logout_user(request):
    try:
        logout(request)
        return render(request, 'logout.html', {})
    except:
        messages.error(request, "Logout Url Page Error Occurred") 
        

def register_user(request):
    try:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, ('Registration Successfully!!!'))
        else:
            form = UserCreationForm()
        return render(request, 'register.html', {'form':form})
    except:
        messages.error(request, "Register Url Page Error Occurred")