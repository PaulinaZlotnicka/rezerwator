from django.db import models
from django.contrib.auth.models import User

CAR_TYPE = (
    (1, "camper"),
    (2, "dostawczy"),
    (3, "osobowy"),
)

SEASON = (
    (1, 'niski 1.01-24.04'),
    (2, 'wysoki 25.04-8.05'),
    (3, 'średni 9.05-5.06'),
    (4, 'wysoki 6.06-31.08'),
    (5, 'średni 1.09-30.09'),
    (6, 'niski 1.10-31.12'),
    (7, 'bez znaczenia'),
)

KM_LIMIT = (
    (1, '200km dziennie'),
    (2, '400 km dziennie'),
    (3, "bez limitu"),
)

CONFIRM = (
    (1, 'zapytanie wysłane'),
    (2, 'potwierdzona')
)

class Cars(models.Model):
    car_model = models.CharField(max_length=200)
    car_type = models.IntegerField(choices=CAR_TYPE)
    description = models.TextField()
    sits = models.SmallIntegerField()
    engine = models.CharField(max_length=100)
    deposit = models.SmallIntegerField()

    def __str__(self):
        return f"{self.car_model} {self.car_type} has {self.sits} sits and engine {self.engine}"


class PriceCarDay(models.Model):
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    season = models.IntegerField(choices = SEASON)
    km_limit = models.IntegerField(choices = KM_LIMIT)
    price_per_day = models.IntegerField()

class Message(models.Model):
    content = models.CharField(max_length=280)
    creation_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "author")
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.author} to {self.recipient} on {self.creation_date} tweeted {self.content[:10]} read {self.read}"

class CarReservation(models.Model):
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    confirmed = models.IntegerField(choices = CONFIRM)
