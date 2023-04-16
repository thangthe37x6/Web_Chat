from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm,RegistrationForm
from .models import question

def test(request):
    topics = question.objects.values('chude').distinct()
    return render(request, 'test.html', {'topics': topics})

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html', {'form': form})
def register(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()
        login(request, new_user)
        return redirect('home')
    return render(request, 'register.html', {'form': form})

def logout(request):
    pass
def home(request):
    return render(request, 'home.html', {})

