from django.db import models


# Create your models here.

class HouseHold (models.Model):
    Name = models.CharField(max_length=64)


    def __str__(self):
        return f"{self.id} {self.name}"
