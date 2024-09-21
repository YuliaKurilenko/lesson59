from django.db import models

# class Buyer(models.Model):
#     name = models.CharField(max_length=30)
#     balance = models.DecimalField(max_digits=8,decimal_places=2)
#     age = models.IntegerField()
#
#     def __str__(self):
#         return self.name
#
# class Game(models.Model):
#     title = models.CharField(max_length=30)
#     cost = models.DecimalField(max_digits=5, decimal_places=2)
#     size = models.DecimalField(max_digits=5, decimal_places=2)
#     description = models.TextField()
#     age_limited = models.BooleanField(default=False)
#     buyer = models.ManyToManyField(Buyer, related_name='game')

class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()


    def __str__(self):
        return self.name
# Create your models here

