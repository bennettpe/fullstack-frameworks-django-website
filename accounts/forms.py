#Form for users to register

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UserLoginForm(forms.Form):
    """Form Used to log users in """
    
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):  
    """Form Used to register a new user"""
    
    password1 = forms.CharField(
        label="Password", 
        widget=forms.PasswordInput
        )
    password2 = forms.CharField(
        label="Password Confirmation", 
        widget=forms.PasswordInput
        )
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

   
    def clean_email(self):  
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        
        if not email:
            raise ValidationError("Email address must not be empty")
            
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email address must be unique')    
            
        return email

        
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if not password1 or not password2:
            raise ValidationError("Password must not be empty")
            
        if password1 != password2:
            raise ValidationError("Passwords do not match")
            
        return password2