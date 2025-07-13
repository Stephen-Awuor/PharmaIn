from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CreateUserForm  # <-- use your custom form
from django.contrib.auth.decorators import login_required

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

