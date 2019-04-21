# Products related urls

from django.conf.urls import url, include
from products.views import products, body, brake, clutch, cooling, gearbox, electrical, engine, exhaust, \
                           exterior, fuel, interior, overdrive, roadwheels, service, steering, suspfront, susprear   
                              
urlpatterns = [
    url(r'^categories/$', products, name='products'),
    url(r'^body/$', body, name='body'),
    url(r'^brake/$', brake, name='brake'),
    url(r'^clutch/$', clutch, name='clutch'),
    url(r'^cooling/$', cooling, name='cooling'),
    url(r'^electrical/$', electrical, name='electrial'), 
    url(r'^engine/$', engine, name='engine'),
    url(r'^exhaust/$', exhaust, name='exhaust'),
    url(r'^exterior/$', exterior, name='exterior'),
    url(r'^fuel/$', fuel, name='fuel'),
    url(r'^interior/$', interior, name='interior'),
    url(r'^overdrive/$', interior, name='overdrive'),
    url(r'^roadwheels/$', roadwheels, name='roadwheels'),
    url(r'^service/$', service, name='service'),
    url(r'^steering/$', steering, name='steering'),
    url(r'^suspfront/$', suspfront, name='suspfront'),
    url(r'^susprear/$', susprear, name='susprear'),
]    