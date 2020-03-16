from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# FLAT_CHOICES = ( 
#     ("1", "1"), 
#     ("2", "2"), 
#     ("3", "3"), 
#     ("4", "4"), 
#     ("5", "5"), 
#     ("6", "6"), 
#     ("7", "7"), 
#     ("8", "8"),
#     ("9", "9"),
#     ("10", "10"),
#     ("11", "11"),
#     ("12", "12"),
#     ("13", "13"),
#     ("14", "14"), 
# ) 

class Resident(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(default='example@gmail.com')
    #flatNo1 = models.IntegerField(default=0, choices=FLAT_CHOICES)
    #flatNo2 = models.IntegerField(default=0, choices=FLAT_CHOICES)
    flatNo1 = models.CharField(max_length=5)
    flatNo2 = models.CharField(max_length=5)
    phone = models.CharField(max_length=10)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    isOwner = models.BooleanField(default=False)
    multipleFlats = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)