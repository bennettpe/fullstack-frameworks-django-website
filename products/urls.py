# Products related urls

from django.conf.urls import url, include
from products.views import products, engine, clutch, gearbox, cooling, fuel, steering, suspfront, susprear, brake, \
                           exhaust, electrics, interior, exterior, body

urlpatterns = [
    url(r'^categories/$', products, name='categories'),
    url(r'^engine/$', engine, name='engine'),
    url(r'^clutch/$', clutch, name='clutch'),
    url(r'^gearbox/$', gearbox, name='gearbox'),
    url(r'^cooling/$', cooling, name='cooling'),
    url(r'^fuel/$', fuel, name='fuel'),
    url(r'^steering/$', steering, name='steering'),
    url(r'^suspfront/$', suspfront, name='suspfront'),
    url(r'^susprear/$', susprear, name='susprear'),
    url(r'^brake/$', brake, name='brake'),
    url(r'^exhaust/$', exhaust, name='exhaust'),
    url(r'^electrics/$', electrics, name='electrics'), 
    url(r'^interior/$', interior, name='interior'),
    url(r'^exterior/$', exterior, name='exterior'),
    url(r'^body/$', body, name='body')
]