from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    wallet = models.PositiveIntegerField(default=1000)

    def __str__(self):
        return f'Name: {self.username}'


class Hall(models.Model):
    name = models.CharField(max_length=50)
    size = models.PositiveIntegerField()

    def __str__(self):
        return f'Name: {self.name} Size: {self.size}'


class Ticket(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    screening_date = models.DateTimeField()
    price = models.PositiveIntegerField()
    rest_of_seats = models.PositiveIntegerField()

    def __str__(self):
        return f'Name: {self.name} Price: {self.price}'


class Purchase(models.Model):
    amount = models.PositiveIntegerField()
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Amount: {self.amount} by {self.buyer}'
