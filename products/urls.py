# Products related urls

from django.conf.urls import url, include
from products.views import products, alt_dyno, body, brakes, brakes_fr, brakes_handbrake, \
                           clutch, cooling, crankshaft, electrical, engine, exhaust, exterior, \
                           fuel, gearbox, gearbox_mk4, gearbox_1500, interior, oilsump, overdrive, \
                           overdrive_j, roadwheels, service, steering, suspfront, susprear   
                              
urlpatterns = [
    url(r'^categories/$', products, name='products'),
    url(r'^alt_dyno/$', alt_dyno, name='alt_dyno'),
    url(r'^body/$', body, name='body'),
    url(r'^brakes/$', brakes, name='brakes'),
    url(r'^brakes_fr/$', brakes_fr, name='brakes_fr'),
    url(r'^brakes_handbrake/$', brakes_handbrake, name='brakes_handbrake'),
    url(r'^clutch/$', clutch, name='clutch'),
    url(r'^cooling/$', cooling, name='cooling'),
    url(r'^crankshaft/$', crankshaft, name='crankshaft'),
    url(r'^electrical/$', electrical, name='electrical'), 
    url(r'^engine/$', engine, name='engine'),
    url(r'^exhaust/$', exhaust, name='exhaust'),
    url(r'^exterior/$', exterior, name='exterior'),
    url(r'^fuel/$', fuel, name='fuel'),
    url(r'^gearbox/$', gearbox, name='gearbox'),
    url(r'^gearbox_mk4/$', gearbox_mk4, name='gearbox_mk4'),
    url(r'^gearbox_1500/$', gearbox_1500, name='gearbox_1500'),
    url(r'^interior/$', interior, name='interior'),
    url(r'^oilsump/$', oilsump, name='oilsump'),
    url(r'^overdrive/$', overdrive, name='overdrive'),
    url(r'^overdrive_j/$', overdrive_j, name='overdrive_j'),
    url(r'^roadwheels/$', roadwheels, name='roadwheels'),
    url(r'^service/$', service, name='service'),
    url(r'^steering/$', steering, name='steering'),
    url(r'^suspfront/$', suspfront, name='suspfront'),
    url(r'^susprear/$', susprear, name='susprear'),
]  