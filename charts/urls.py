from django.conf.urls import url
from .views import charts

urlpatterns = [
    url(r'^$', charts, name='charts'),
]