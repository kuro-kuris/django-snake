from django.db import models




class User(models.Model):
    username = models.CharField(max_length=200)
    budget = models.IntegerField(default=0)

    def __str__(self):
    	return self.username

class Saving_Account(models.Model):
    balance = models.IntegerField(default=0)
    username = models.ForeignKey(User)

    def __str__(self):
    	return (self.username + " savings account with " + self.balance)

class Pet(models.Model):
    username = models.ForeignKey(User)
    name = models.CharField(max_length=200)
    pet_health = models.IntegerField(default=100)
    virtual_gold = models.IntegerField(default=0)
    level = models.IntegerField(default=0)
    experience = models.IntegerField(default=0)
