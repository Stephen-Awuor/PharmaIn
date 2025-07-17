from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from django.contrib.auth.forms import PasswordChangeForm



class CreateUserForm(UserCreationForm):
    is_staff = forms.BooleanField(required=False, label="Is Admin?")
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'username', 'password1', 'password2', 'is_staff']

class EmailLoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))

class UpdateUserForm(forms.ModelForm):
    is_staff = forms.BooleanField(required=False, label="Is Admin?")
    new_password = forms.CharField(
        required=False,
        label="New Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text="Leave blank to keep current password."
    )
    confirm_password = forms.CharField(
        required=False,
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'username', 'is_staff']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("new_password")
        confirm = cleaned_data.get("confirm_password")
        if password and password != confirm:
            self.add_error("confirm_password", "Passwords do not match.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('new_password')
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user
    
class EditMyProfileForm(forms.ModelForm):
    new_password = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False
    )
    confirm_password = forms.CharField(
        label='Confirm New Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'new_password', 'confirm_password']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(EditMyProfileForm, self).__init__(*args, **kwargs)

        # Debug print (temporary)
        print("User is staff:", user.is_staff if user else 'no user')

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

        # Only make read-only for non-admins
        if user and not user.is_staff:
            self.fields['first_name'].widget.attrs['readonly'] = True
            self.fields['last_name'].widget.attrs['readonly'] = True
            self.fields['email'].widget.attrs['readonly'] = True





