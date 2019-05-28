from django.shortcuts import render
from products.models import Product, UserRating
from accounts.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.contrib import messages

import json

#RATE PRODUCT 
@login_required   
def ratings(request):
    if request.method == 'POST':
        success = False
        part_number = request.POST.get('part_number') # From JS var data
        button_clicked = request.POST.get('button')
        
        # User has rated this product so update current rating
        try:
            current_rating = UserRating.objects.get(product__part_number = part_number, user_profile__user__username = request.user.username)
            product = current_rating.product
            
            if button_clicked in ['liked', 'disliked']:
                current_rating.rating = button_clicked
                current_rating.save()
                new_liked = len(UserRating.objects.filter(product=product, rating='liked'))
                new_disliked = len(UserRating.objects.filter(product=product, rating='disliked'))
                success = True
                
        # User has not rated this product yet so create a user rating      
        except UserRating.DoesNotExist:
            product = Product.objects.get(part_number = part_number)
            user_profile = UserProfile.objects.get(user = request.user)
            
            if product and user_profile:
                UserRating.objects.create(product=product, user_profile=user_profile, rating=button_clicked)
                new_liked = len(UserRating.objects.filter(product=product, rating='liked'))
                new_disliked = len(UserRating.objects.filter(product=product, rating='disliked'))
                success = True
            
            # Handle what happens if you cannot find the product or the profile (should never happen, but just in case)
            else:
                success = False
                
        response = {
            'success': success,
            'new_liked': new_liked,
            'new_disliked': new_disliked
        }
        return HttpResponse(json.dumps(response), content_type="application/json")
        
    raise Http404('Invalid Request Method')

# Create your views here.
def products(request):
    return render(request, 'categories.html')

# Product.objects.filter() will find all the product entries in the database whose category=engine
# Then assign them to a 'products_list' variable and send that variable to engine.html template

#ALTERNATOR & DYNAMO
def alt_dyno(request):
    return render(request, 'alt_dyno.html', 
    {'products_list': Product.objects.filter(category='alt_dyno').order_by('part_name','part_number')}) 

#BODY
def body(request):
    return render(request, 'body.html', 
    {'products_list': Product.objects.filter(category='body').order_by('part_name','part_number')}) 

#BONNET
def bonnet(request):
    return render(request, 'bonnet.html', 
    {'products_list': Product.objects.filter(category='bonnet').order_by('part_name','part_number')})     

#BOOT
def boot(request):
    return render(request, 'boot.html', 
    {'products_list': Product.objects.filter(category='boot').order_by('part_name','part_number')})  

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
    {'products_list': Product.objects.filter(category='brakes_hand').order_by('part_name','part_number')})   

#BUMPERS
def bumpers(request):
    return render(request, 'bumpers.html', 
    {'products_list': Product.objects.filter(category='bumpers').order_by('part_name','part_number')})     

#CHARGING_STARTING
def charging(request):
    return render(request, 'charging.html', 
    {'products_list': Product.objects.filter(category='charging').order_by('part_name','part_number')})     

#CHASSIS
def chassis(request):
    return render(request, 'chassis.html', 
    {'products_list': Product.objects.filter(category='chassis').order_by('part_name','part_number')})   

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

#DOOR
def door(request):
    return render(request, 'door.html', 
    {'products_list': Product.objects.filter(category='door').order_by('part_name','part_number')})      

#DASHBOARD
def dashboard(request):
    return render(request, 'dashboard.html', 
    {'products_list': Product.objects.filter(category='dashboard').order_by('part_name','part_number')})   

#DRIVE_LINE
def drive_line(request):
    return render(request, 'drive_line.html', 
    {'products_list': Product.objects.filter(category='drive_line').order_by('part_name','part_number')}) 

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

#EXTERNAL
def external(request):
    return render(request, 'external.html', 
    {'products_list': Product.objects.filter(category='external').order_by('part_name','part_number')})     

#FUEL SYSTEM
def fuel(request):
    return render(request, 'fuel.html', 
    {'products_list': Product.objects.filter(category='fuel').order_by('part_name','part_number')})   

#FUEL PIPES
def fuel_pipes(request):
    return render(request, 'fuel_pipes.html', 
    {'products_list': Product.objects.filter(category='fuel_pipes').order_by('part_name','part_number')})     

#FUEL TANK
def fuel_tank(request):
    return render(request, 'fuel_tank.html', 
    {'products_list': Product.objects.filter(category='fuel_tank').order_by('part_name','part_number')}) 

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

#HARDTOP
def hardtop(request):
    return render(request, 'hardtop.html', 
    {'products_list': Product.objects.filter(category='hardtop').order_by('part_name','part_number')})   

#HOOD
def hood(request):
    return render(request, 'hood.html', 
    {'products_list': Product.objects.filter(category='hood').order_by('part_name','part_number')}) 

#HEATING
def heating(request):
    return render(request, 'heating.html', 
    {'products_list': Product.objects.filter(category='heating').order_by('part_name','part_number')})

#IGNITION
def ignition(request):
    return render(request, 'ignition.html', 
    {'products_list': Product.objects.filter(category='ignition').order_by('part_name','part_number')})     

#INSTRUMENT ANS SWITCHES
def inst_sw(request):
    return render(request, 'inst_sw.html', 
    {'products_list': Product.objects.filter(category='inst_sw').order_by('part_name','part_number')}) 

#INNER BODY
def inner_body(request):
    return render(request, 'inner_body.html', 
    {'products_list': Product.objects.filter(category='inner_body').order_by('part_name','part_number')}) 

#INTERIOR
def interior(request):
    return render(request, 'interior.html', 
    {'products_list': Product.objects.filter(category='interior').order_by('part_name','part_number')}) 

#LAMPS
def lamps(request):
    return render(request, 'lamps.html', 
    {'products_list': Product.objects.filter(category='lamps').order_by('part_name','part_number')}) 

#MOULDINGS
def mouldings(request):
    return render(request, 'mouldings.html', 
    {'products_list': Product.objects.filter(category='mouldings').order_by('part_name','part_number')})     

#OIL SUMP
def oilsump(request):
    return render(request, 'oilsump.html', 
    {'products_list': Product.objects.filter(category='oil_sump').order_by('part_name','part_number')})    

#OVERDRIVE
def overdrive(request):
    return render(request, 'overdrive.html', 
    {'products_list': Product.objects.filter(category='overdrive').order_by('part_name','part_number')})

#OVERDRIVE_J
def overdrive_j(request):
    return render(request, 'overdrive_j.html', 
    {'products_list': Product.objects.filter(category='overdrive_j').order_by('part_name','part_number')})    

#OUTER BODY
def outer_body(request):
    return render(request, 'outer_body.html', 
    {'products_list': Product.objects.filter(category='outer_body').order_by('part_name','part_number')}) 

#RADIATOR GRILL
def rad_grill(request):
    return render(request, 'rad_grill.html', 
    {'products_list': Product.objects.filter(category='rad_grill').order_by('part_name','part_number')})     

#ROADWHEELS
def road_wheels(request):
    return render(request, 'road_wheels.html', 
    {'products_list': Product.objects.filter(category='road_wheels').order_by('part_name','part_number')})       

#SEATS
def seats(request):
    return render(request, 'seats.html', 
    {'products_list': Product.objects.filter(category='seats').order_by('part_name','part_number')}) 

#STEERING
def steering(request):
    return render(request, 'steering.html', 
    {'products_list': Product.objects.filter(category='steering').order_by('part_name','part_number')}) 

#SUSPENSION
def suspension(request):
    return render(request, 'suspension.html', 
    {'products_list': Product.objects.filter(category='suspension').order_by('part_name','part_number')})     

#TRIM KITS
def trim_kits(request):
    return render(request, 'trim_kits.html', 
    {'products_list': Product.objects.filter(category='trim_kits').order_by('part_name','part_number')}) 

#WINDSCREEN 
def windscreen(request):
    return render(request, 'windscreen.html', 
    {'products_list': Product.objects.filter(category='windscreen').order_by('part_name','part_number')})     

#WINDSCREEN WIPERS & WASHER
def wshld_wipe_wash(request):
    return render(request, 'wshld_wipe_wash.html', 
    {'products_list': Product.objects.filter(category='wshld_wipe_wash').order_by('part_name','part_number')})      

#WIRING AND INTERNAL ELECTRICS
def wire_int(request):
    return render(request, 'wire_int.html', 
    {'products_list': Product.objects.filter(category='wire_int').order_by('part_name','part_number')}) 