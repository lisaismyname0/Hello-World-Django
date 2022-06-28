from re import L
from django.db import models
from django.contrib.auth.models import AbstractUser
#this means i want django's built in abstract user


class User(AbstractUser):
    pass
    #what we put here structures the table that SQL builds


class Flavor(models.Model):
    name = models.CharField(max_length=100)
    flavor_description = models.CharField(max_length=150, blank=True, null=True)
    local = models.BooleanField(null=True)
    season = models.ForeignKey(to="Season", on_delete=models.CASCADE, blank=True, null=True)
    #putting Type in quotes allows us to reference the variable before we've called it.


    class Meta:
        verbose_name_plural = "Flavours"
        #this allowed me to override the django admin view's natural pluralization (simply adding an s) and allowed me to specify my pluralization
    def __str__(self):
        return self.name
        #adding this string method allowed me to change the name of my flavor instance in my django admin from flavor object to its name


class Season(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
