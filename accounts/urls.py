from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import EmailLoginForm

urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html',authentication_form=EmailLoginForm), name='login'),
    #  path('dashboard/', views.dashboard, name='dashboard'),
    # path('register/', views.register, name='register'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
