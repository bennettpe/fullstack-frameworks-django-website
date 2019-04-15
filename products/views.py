from django.shortcuts import render
from products.models import Product

# Create your views here.
def products(request):
    return render(request, 'categories.html')

# Product.objects.filter() will find all the product entries in the database whose category=engine
# Then assign them to a 'products_list' variable and send that variable to engine.html template

#ENGINE
def engine(request):
    return render(request, 'engine.html', 
    {'products_list': Product.objects.filter(category='engine')})
#CLUTCH
def clutch(request):
    return render(request, 'clutch.html', 
    {'products_list': Product.objects.filter(category='clutch')})
#GEARBOX
def gearbox(request):
    return render(request, 'gearbox.html', 
    {'products_list': Product.objects.filter(category='gearbox')})
#COOLING SYSTEM
def cooling(request):
    return render(request, 'cooling.html', 
    {'products_list': Product.objects.filter(category='cooling')})
#FUEL SYSTEM
def fuel(request):
    return render(request, 'fuel.html', 
    {'products_list': Product.objects.filter(category='fuel')})   
#STEERING
def steering(request):
    return render(request, 'steering.html', 
    {'products_list': Product.objects.filter(category='steering')})     
#FRONT SUSPENSION
def suspfront(request):
    return render(request, 'suspfront.html', 
    {'products_list': Product.objects.filter(category='suspfront')})   
#REAR SUSPENSION
def susprear(request):
    return render(request, 'susprear.html', 
    {'products_list': Product.objects.filter(category='susprear')})  
#BRAKE SYSTEM
def brake(request):
    return render(request, 'brake.html', 
    {'products_list': Product.objects.filter(category='brake')})  
#EXHAUST SYSTEM
def exhaust(request):
    return render(request, 'exhaust.html', 
    {'products_list': Product.objects.filter(category='exhaust')}) 
#ELECTRICS
def electrics(request):
    return render(request, 'electrics.html', 
    {'products_list': Product.objects.filter(category='electrics')})      
#INTERIOR
def interior(request):
    return render(request, 'interior.html', 
    {'products_list': Product.objects.filter(category='interior')})     
#EXTERIOR
def exterior(request):
    return render(request, 'exterior.html', 
    {'products_list': Product.objects.filter(category='exterior')}) 
#BODY & CHASSIS
def body(request):
    return render(request, 'body.html', 
    {'products_list': Product.objects.filter(category='body')})    