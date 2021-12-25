from django.db import models


class Factory(models.Model):
    name = models.CharField(max_length=10)


class Car(models.Model):
    COLOR_CHOICES = (("b", "black"), ("w", "white"))
    name = models.CharField(max_length=10)
    color = models.CharField(choices=COLOR_CHOICES,max_length=10)
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, max_length=10)
    price = models.IntegerField()
