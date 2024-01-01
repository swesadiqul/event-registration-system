from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from . forms import *


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Log the user in after signup (optional)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            
            # Redirect to a success page or home
            return redirect('home')
    return render(request, 'accounts/signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('accounts:dashboard'))
        else:
            return render(request, 'accounts/login.html')

    return render(request, 'accounts/login.html')


def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('events:home'))


@login_required(login_url='accounts:login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')


@login_required(login_url='accounts:login')
def profile_update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:dashboard')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'accounts/profile_update.html', {'form': form})