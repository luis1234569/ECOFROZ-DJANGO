from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .forms import UserLoginForm

# Create your views here.

###############LOGIN#####################

def login(request):
    form = UserLoginForm
    
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

        
            user = authenticate(username=username, password=password)
            if user is not None:
                do_login(request, user)
                return redirect('landing')
           
            else:
                return redirect('home')
        
        else:
            # return HttpResponse("La contraseña no es correcta!!")
            return render(request, 'registration/login.html', {'form': form})
            
    else:
        if request.user.is_authenticated:
            return redirect ('landing')
        else:
            return render(request, 'registration/login.html', {'form': form})

def logout(request):
    do_logout(request)
    return redirect('home')

class Inicio(TemplateView):
    template_name = 'index.html'

class LandingPage(LoginRequiredMixin, TemplateView):
    template_name = 'landing.html'

class EnConstruccion(LoginRequiredMixin, TemplateView):
    template_name = 'construccion.html'

class Sia(LoginRequiredMixin, TemplateView):
    template_name = 'index_sia.html'