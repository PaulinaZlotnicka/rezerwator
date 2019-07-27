from django.contrib import admin
from .models import Cars, PriceCarDay, Message, CarReservation

@admin.register(Cars)
class CarsAdmin(admin.ModelAdmin):
    list_display = ("car_model", "car_type", "sits", "deposit")

@admin.register(PriceCarDay)
class PriceAdmin(admin.ModelAdmin):
    list_display = ("car", "season", "km_limit", "price_per_day")

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("author", "recipient", "creation_date", "content")

@admin.register(CarReservation)
class CarReservationAdmin(admin.ModelAdmin):
    list_display = ('car', 'message', 'user', 'start_date', "end_date", "confirmed")
