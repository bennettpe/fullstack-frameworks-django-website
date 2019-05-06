from accounts.forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth, messages
from django.shortcuts import render, redirect, reverse


# Create your views here.
def index(request):
    """Return the index.html file"""
    return render(request, 'index.html')
    
# The 'logoin' view allows users to login 
def login(request):
    """Log the user in"""
    if request.user.is_authenticated:
         return redirect(reverse('index')) #Redirect to index page
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
                                     
            if user:
                auth.login(user=user, request=request)
                
                
                return redirect(reverse('index')) #Redirect to index page
            else:
                login_form.add_error(None, "Your username or password is incorrect")
                
    else:
        login_form = UserLoginForm()
        
    return render(request, 'login.html', {"login_form": login_form})


# The 'logout' view allows users to logout
@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('index')) #Redirect to index page

    
# The 'registration' view allows user to register
def registration(request):
    """Manages the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index')) #Redirect to index page
        
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        
        if registration_form.is_valid():
            registration_form.save()
            
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have sucessfully registered")
                return redirect(reverse('index')) #Redirect to index page
            else:
                messages.error(request, "Unable to register your account at this time")
    else:      
        registration_form = UserRegistrationForm()
        
    return render(request, 'registration.html', {"registration_form": registration_form})
    
def user_profile(request):
    """The user's profile page"""
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile.html', {"profile": user})
    