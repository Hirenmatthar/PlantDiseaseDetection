from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

def home(request):
    return render(request, 'index.html')

def register(request):
    initial_data = {'username':'','password1':'','password2':''}
    form = UserCreationForm(initial=initial_data)
    return render(request, 'auth/register.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        initial_data = {'username':'','password1':'','password2':''}
        form = UserCreationForm(initial=initial_data)
    return render(request,'auth/register.html',{'form':form})
    
def login(request):
    initial_data = {'username':'','password':''}
    form = AuthenticationForm(initial=initial_data)
    return render(request, 'auth/login.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request,user)
            return redirect('/home/')
    else:
        initial_data = {'username':'','password':''}
        form = AuthenticationForm(initial=initial_data)
    return render(request,'auth/login.html',{'form':form})

def logout(request):
    logout(request)
    return redirect('login')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')
