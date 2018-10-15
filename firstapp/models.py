from django.db import models
from datetime import datetime    

# Create your models here.
class Person(models.Model):
    firstname= models.CharField(max_length=20,unique=True)
    lastname= models.CharField(max_length=15,null=True)
    dob=models.DateField(default=datetime.now)
    phonenumber=models.IntegerField()
    email = models.EmailField(max_length=70,unique=True)

    def __str__(self):
        return self.firstname