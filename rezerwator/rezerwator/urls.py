"""rezerwator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from reservation_app.views import Main, Available_campers, Available_van, Available_pass, CarDetails, AvailableCar, MakeReservation

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', Main.as_view(), name='main'),
    path('availability/campers/', Available_campers.as_view(), name='available-campers'),
    path('availability/vans/', Available_van.as_view(), name='available-vans'),
    path('availability/passengers/', Available_pass.as_view(), name='available-campers'),
    url(r'^availability/(?P<pk>\d+)/$', AvailableCar.as_view(), name='available-car'),
    url(r'^car_details/(?P<pk>\d+)/$', CarDetails.as_view(), name='car-details'),
    url(r'^makereservation/(?P<pk>\d+)/$', MakeReservation.as_view(), name='make-reservation'),
]
