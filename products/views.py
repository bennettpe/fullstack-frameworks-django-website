from django.shortcuts import render
from products.models import Product

# Create your views here.
def products(request):
    return render(request, 'categories.html')

# Product.objects.filter() will find all the product entries in the database whose category=engine
# Then assign them to a 'products_list' variable and send that variable to engine.html template

#ALTERNATOR & DYNAMO
def alt_dyno(request):
    return render(request, 'alt_dyno.html', 
    {'products_list': Product.objects.filter(category='alt_dyno').order_by('part_name','part_number')}) 
#BODY & CHASSIS
def body(request):
    return render(request, 'body.html', 
    {'products_list': Product.objects.filter(category='body').order_by('part_name','part_number')}) 
#BRAKE SYSTEM
def brakes(request):
    return render(request, 'brakes.html', 
    {'products_list': Product.objects.filter(category='brakes').order_by('part_name','part_number')}) 
#BRAKE FRONT & REAR
def brakes_fr(request):
    return render(request, 'brakes_fr.html', 
    {'products_list': Product.objects.filter(category='brakes_fr').order_by('part_name','part_number')}) 
#BRAKE HANDBRAKE
def brakes_handbrake(request):
    return render(request, 'brakes_handbrake.html', 
    {'products_list': Product.objects.filter(category='brakes_handbrake').order_by('part_name','part_number')})   
#CHARGING_STARTING
def charging(request):
    return render(request, 'charging.html', 
    {'products_list': Product.objects.filter(category='charging').order_by('part_name','part_number')})     
#CLUTCH
def clutch(request):
    return render(request, 'clutch.html', 
    {'products_list': Product.objects.filter(category='clutch').order_by('part_name','part_number')}) 
#COOLING SYSTEM
def cooling(request):
    return render(request, 'cooling.html', 
    {'products_list': Product.objects.filter(category='cooling').order_by('part_name','part_number')})
#CRANKSHAFT
def crankshaft(request):
    return render(request, 'crankshaft.html', 
    {'products_list': Product.objects.filter(category='crankshaft').order_by('part_name','part_number')})     
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
#GEARBOX_MK3
def gearbox(request):
    return render(request, 'gearbox.html', 
    {'products_list': Product.objects.filter(category='gearbox').order_by('part_name','part_number')})
#GEARBOX_MK4
def gearbox_mk4(request):
    return render(request, 'gearbox_mk4.html', 
    {'products_list': Product.objects.filter(category='gearbox_mk4').order_by('part_name','part_number')})
#GEARBOX_1500
def gearbox_1500(request):
    return render(request, 'gearbox_1500.html', 
    {'products_list': Product.objects.filter(category='gearbox_1500').order_by('part_name','part_number')})    
#INTERIOR
def interior(request):
    return render(request, 'interior.html', 
    {'products_list': Product.objects.filter(category='interior').order_by('part_name','part_number')}) 
#OIL SUMP
def oilsump(request):
    return render(request, 'oilsump.html', 
    {'products_list': Product.objects.filter(category='oilsump').order_by('part_name','part_number')})    
#OVERDRIVE
def overdrive(request):
    return render(request, 'overdrive.html', 
    {'products_list': Product.objects.filter(category='overdrive').order_by('part_name','part_number')})
#OVERDRIVE_J
def overdrive_j(request):
    return render(request, 'overdrive_j.html', 
    {'products_list': Product.objects.filter(category='overdrive_j').order_by('part_name','part_number')})    
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