from django.db import models

# Create your models here.
class Zurischool(models.Model):
    name = models.CharField(max_length=23)
    address = models.CharField(max_length=23)

    def __str__(self) -> str:
        return self.name

class State(models.Model):
    name = models.CharField(max_length=23)

    def __str__(self) -> str:
        return self.name