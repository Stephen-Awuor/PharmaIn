from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CreateUserForm  
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import User

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully.')
            return redirect('login')
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html') 

def logoutUser(request):
    logout(request)
    return redirect('login')  

@login_required
def users_list(request):
    users = User.objects.all()
    return render(request, 'accounts/users.html', {'users': users})
