from django.shortcuts import render, redirect, reverse

# Create your views here.

# VIEW about
def about(request):
    return render(request, 'about.html')