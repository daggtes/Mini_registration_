from django.db import models


# Create your models here.

class HouseHold (models.Model):
    Name = models.CharField(max_length=64)
    

    def __str__(self):
        return f"{self.id} {self.Name}"

class New (models.Model):
    Name = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    age = models.IntegerField(null=True)
    number = models.IntegerField(null=True)


    def __str__(self):
        return f"{self.id} {self.Name} {self.lastname} {self.age}" 
