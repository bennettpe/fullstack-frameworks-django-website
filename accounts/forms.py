#Form for users to register

from django import forms
# you need to add this line below if you have extended user model so it 
# picks up password validation settings in settings.py
from django.contrib.auth import password_validation
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

    # Check password validation
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        
        password_validation.validate_password(
           self.cleaned_data['password1'],
           self.instance)
        
        return password1
    
    # Check if passwords are not empty 
    # Check if passwords match
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        # Check password validation
        password_validation.validate_password(
           self.cleaned_data['password2'],
           self.instance)
        
        if not password1 or not password2:
            raise ValidationError("Password must not be empty")
            
        if password1 != password2:
            raise ValidationError("Passwords do not match")
            
        return password2