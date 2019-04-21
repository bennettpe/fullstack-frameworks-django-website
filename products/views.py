from django.shortcuts import render
from products.models import Product

# Create your views here.
def products(request):
    return render(request, 'categories.html')

# Product.objects.filter() will find all the product entries in the database whose category=engine
# Then assign them to a 'products_list' variable and send that variable to engine.html template

#BODY & CHASSIS
def body(request):
    return render(request, 'body.html', 
    {'products_list': Product.objects.filter(category='body').order_by('part_name','part_number')}) 
#BRAKE SYSTEM
def brake(request):
    return render(request, 'brake.html', 
    {'products_list': Product.objects.filter(category='brake').order_by('part_name','part_number')}) 
#CLUTCH
def clutch(request):
    return render(request, 'clutch.html', 
    {'products_list': Product.objects.filter(category='clutch').order_by('part_name','part_number')}) 
#COOLING SYSTEM
def cooling(request):
    return render(request, 'cooling.html', 
    {'products_list': Product.objects.filter(category='cooling').order_by('part_name','part_number')})
#ENGINE
def engine(request):
    return render(request, 'engine.html', 
    {'products_list': Product.objects.filter(category='engine').order_by('part_name','part_number')})
#ELECTRICAL
def electrical(request):
    return render(request, 'electrical.html', 
    {'products_list': Product.objects.filter(category='electrical').order_by('part_name','part_number')})      
#EXHAUST SYSTEM
def exhaust(request):
    return render(request, 'exhaust.html', 
    {'products_list': Product.objects.filter(category='exhaust').order_by('part_name','part_number')})
#EXTERIOR
def exterior(request):
    return render(request, 'exterior.html', 
    {'products_list': Product.objects.filter(category='exterior').order_by('part_name','part_number')})     
#FRONT SUSPENSION
def suspfront(request):
    return render(request, 'suspfront.html', 
    {'products_list': Product.objects.filter(category='suspfront').order_by('part_name','part_number')})      
#FUEL SYSTEM
def fuel(request):
    return render(request, 'fuel.html', 
    {'products_list': Product.objects.filter(category='fuel').order_by('part_name','part_number')})   
#GEARBOX
def gearbox(request):
    return render(request, 'gearbox.html', 
    {'products_list': Product.objects.filter(category='gearbox').order_by('part_name','part_number')})
#INTERIOR
def interior(request):
    return render(request, 'interior.html', 
    {'products_list': Product.objects.filter(category='interior').order_by('part_name','part_number')}) 
#OVERDRIVE
def overdrive(request):
    return render(request, 'overdrive.html', 
    {'products_list': Product.objects.filter(category='overdrive').order_by('part_name','part_number')})
#REAR SUSPENSION
def susprear(request):
    return render(request, 'susprear.html', 
    {'products_list': Product.objects.filter(category='susprear').order_by('part_name','part_number')}) 
#ROADWHEELS
def roadwheels(request):
    return render(request, 'roadwheels.html', 
    {'products_list': Product.objects.filter(category='roadwheels').order_by('part_name','part_number')})       
#SERVICE
def service(request):
    return render(request, 'service.html', 
    {'products_list': Product.objects.filter(category='service').order_by('part_name','part_number')})     
#STEERING
def steering(request):
    return render(request, 'steering.html', 
    {'products_list': Product.objects.filter(category='steering').order_by('part_name','part_number')})   


    
  

   