from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Indomie(models.Model):
    TYPE = (
        ("MG", "Mie Goreng"),
        ("MK", "Mie Kuah"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    amount = models.PositiveIntegerField(default=100)
    description = models.TextField()
    price = models.PositiveIntegerField(default=2500)
    type = models.CharField(max_length=2, choices=TYPE)

    def __str__(self):
        return self.name
