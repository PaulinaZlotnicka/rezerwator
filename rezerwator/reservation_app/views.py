from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, UpdateView, CreateView
from .models import Cars, CAR_TYPE, CarReservation, PriceCarDay, Message
from django.views import View
import datetime
from dateutil import parser

class Main(TemplateView):
    template_name = 'main.html'

    def get_context_data(self):
        campers = Cars.objects.filter(car_type=1)
        vans = Cars.objects.filter(car_type=2)
        passengers = Cars.objects.filter(car_type=3)

        return {'campers': campers,
                'vans': vans,
                'passengers': passengers}

class CarDetails(TemplateView):
    template_name = "details.html"

    def get_context_data(self, pk):
        car = Cars.objects.get(pk=pk)
        return {'car': car,
                'prices': PriceCarDay.objects.filter(car=car)}

class AvailableCar(View):
    def get(self, request, pk):
        ctx = {"text_1": "Wybierz datę:",
               "title": "SPRAWDŹ DOSTEPNOŚĆ",
               "car": Cars.objects.get(pk=pk),
        }
        return render(request, "available_car.html", ctx)

    def post(self, request, pk):
        car = Cars.objects.get(pk=pk)
        min_date = datetime.datetime.now().date()
        reservations_list = []
        if request.POST.get('check_available'):
            start_date = parser.parse(request.POST.get('start')).date()
            end_date = parser.parse(request.POST.get('end')).date()
            if start_date > min_date:
                reservations_list.extend(CarReservation.objects.filter(start_date__gte=start_date)
                                         .filter(end_date__lte=end_date)
                                         .filter(car=car)
                                         )
                reservations_list.extend(CarReservation.objects.filter(start_date__lte=start_date)
                                         .filter(end_date__lte=end_date)
                                         .filter(end_date__gte=start_date)
                                         .filter(car=car)
                                         )
                reservations_list.extend(CarReservation.objects.filter(start_date__gte=start_date)
                                         .filter(start_date__lte=end_date)
                                         .filter(end_date__gte=end_date)
                                         .filter(car=car)
                                         )
                if len(reservations_list)==0:
                    ctx = {"text_2": "AUTO DOSTĘPNE",
                           "text_3": "ZAREZERWUJ",
                           "car": car}

                else:
                    ctx = {"text_2": "AUTO NIEDOSTĘPNE"}

            return render(request, "available_car.html", ctx)

class Available_campers(View):
    def get(self, request):
        ctx = {"text_1": "Wybierz datę:",
               "title": "SPRAWDŹ DOSTEPNOŚĆ CAMPERÓW",
        }
        return render(request, "available.html", ctx)

    def post(self, request):
        campers = Cars.objects.filter(car_type=1)
        min_date = datetime.datetime.now().date()
        reservations_list = []
        available_car = []
        if request.POST.get('check_available'):
            start_date = parser.parse(request.POST.get('start')).date()
            end_date = parser.parse(request.POST.get('end')).date()
            if start_date > min_date:
                for car in campers:
                    reservations_list.extend(CarReservation.objects.filter(start_date__gte=start_date)
                                             .filter(end_date__lte=end_date)
                                             .filter(car=car)
                                             )
                    reservations_list.extend(CarReservation.objects.filter(start_date__lte=start_date)
                                             .filter(end_date__lte=end_date)
                                             .filter(end_date__gte=start_date)
                                             .filter(car=car)
                                             )
                    reservations_list.extend(CarReservation.objects.filter(start_date__gte=start_date)
                                             .filter(start_date__lte=end_date)
                                             .filter(end_date__gte=end_date)
                                             .filter(car=car)
                                             )
                    if len(reservations_list) == 0:
                        available_car.extend(car)

                if available_car == 0:
                    ctx = {"text_2": "AUTA NIEDOSTĘPNE. SPRAWDŹ INNY TERMIN"}

                else:
                    ctx = {"text_2": "DOSTĘPNE AUTA:",
                           "available_cars": available_car}

            return render(request, "available.html", ctx)


class Available_van(View):
    def get(self, request):
        ctx = {"text_1": "Wybierz datę:",
               "title": "SPRAWDŹ DOSTEPNOŚĆ CAMPERÓW",
        }
        return render(request, "available.html", ctx)

    def post(self, request):
        vans = Cars.objects.filter(car_type=2)
        min_date = datetime.datetime.now().date()
        reservations_list = []
        available_car = []
        if request.POST.get('check_available'):
            start_date = parser.parse(request.POST.get('start')).date()
            end_date = parser.parse(request.POST.get('end')).date()
            if start_date > min_date:
                for car in vans:
                    reservations_list.extend(CarReservation.objects.filter(start_date__gte=start_date)
                                             .filter(end_date__lte=end_date)
                                             .filter(car=car)
                                             )
                    reservations_list.extend(CarReservation.objects.filter(start_date__lte=start_date)
                                             .filter(end_date__lte=end_date)
                                             .filter(end_date__gte=start_date)
                                             .filter(car=car)
                                             )
                    reservations_list.extend(CarReservation.objects.filter(start_date__gte=start_date)
                                             .filter(start_date__lte=end_date)
                                             .filter(end_date__gte=end_date)
                                             .filter(car=car)
                                             )
                    if len(reservations_list) == 0:
                        available_car.extend(car)

                if available_car == 0:
                    ctx = {"text_2": "AUTA NIEDOSTĘPNE. SPRAWDŹ INNY TERMIN"}

                else:
                    ctx = {"text_2": "DOSTĘPNE AUTA:",
                           "available_cars": available_car}

            return render(request, "available.html", ctx)

class Available_pass(View):
    def get(self, request):
        ctx = {"text_1": "Wybierz datę:",
               "title": "SPRAWDŹ DOSTEPNOŚĆ CAMPERÓW",
        }
        return render(request, "available.html", ctx)

    def post(self, request):
        passengers = Cars.objects.filter(car_type=2)
        min_date = datetime.datetime.now().date()
        reservations_list = []
        available_car = []
        if request.POST.get('check_available'):
            start_date = parser.parse(request.POST.get('start')).date()
            end_date = parser.parse(request.POST.get('end')).date()
            if start_date > min_date:
                for car in passengers:
                    reservations_list.extend(CarReservation.objects.filter(start_date__gte=start_date)
                                             .filter(end_date__lte=end_date)
                                             .filter(car=car)
                                             )
                    reservations_list.extend(CarReservation.objects.filter(start_date__lte=start_date)
                                             .filter(end_date__lte=end_date)
                                             .filter(end_date__gte=start_date)
                                             .filter(car=car)
                                             )
                    reservations_list.extend(CarReservation.objects.filter(start_date__gte=start_date)
                                             .filter(start_date__lte=end_date)
                                             .filter(end_date__gte=end_date)
                                             .filter(car=car)
                                             )
                    if len(reservations_list) == 0:
                        available_car.extend(car)

                if available_car == 0:
                    ctx = {"text_2": "AUTA NIEDOSTĘPNE. SPRAWDŹ INNY TERMIN"}

                else:
                    ctx = {"text_2": "DOSTĘPNE AUTA:",
                           "available_cars": available_car}

            return render(request, "available.html", ctx)


class MakeReservation(View):
    def get(self, request, pk):
        car = get_object_or_404(Cars, pk=pk)
        ctx = {"car": car,
               "text_1": "REZERWACJA"}
        return render(request, "make_reservation.html", ctx)

    def post(self, request, pk):
        car = get_object_or_404(Cars, pk=pk)
        min_date = datetime.datetime.now().date()
        reservations_list = []
        if request.POST.get('check_available'):
            start_date = parser.parse(request.POST.get('start')).date()
            end_date = parser.parse(request.POST.get('end')).date()
            if start_date > min_date:
                reservations_list.extend(CarReservation.objects.filter(start_date__gte=start_date)
                                         .filter(end_date__lte=end_date)
                                         .filter(car=car)
                                         )
                reservations_list.extend(CarReservation.objects.filter(start_date__lte=start_date)
                                         .filter(end_date__lte=end_date)
                                         .filter(end_date__gte=start_date)
                                         .filter(car=car)
                                         )
                reservations_list.extend(CarReservation.objects.filter(start_date__gte=start_date)
                                         .filter(start_date__lte=end_date)
                                         .filter(end_date__gte=end_date)
                                         .filter(car=car)
                                         )
                if len(reservations_list)==0:
                    message = Message.objects.create(message=request.POST.get('comment'))
                    CarReservation.objects.create(car=car, start_date=start_date, end_date=end_date, message=message)

                    ctx = {"text_2": "ZAREZERWOWANO"}

                else:
                    ctx = {"text_2": "AUTO NIEDOSTĘPNE"}

            return render(request, "make_reservation.html", ctx)
