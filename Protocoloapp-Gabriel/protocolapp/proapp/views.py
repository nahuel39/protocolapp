from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from proapp.models import Visitas

# Create your views here.
def index(request):
    return render (request,'index.html', {'proapp':Visitas.objects.all()})


def registrarUsuario(request):
    if request.method == 'POST':
        form = UserCreationForm (request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate (username=username, password=password)
            login(request, user)
            return redirect('login')    
    else:
        form = UserCreationForm()
        return render(request, 'registration/register.html', {'form':form})


def alertar(request):
    return render(request,'alertar.html')

def home(request):
    return render(request, 'home.html')
    