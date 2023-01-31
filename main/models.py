from django.db import models

from django.contrib.auth.models import User 


# home
class Counter(models.Model):
    countries=models.IntegerField()
    volunteers=models.IntegerField()
    our_goal=models.IntegerField()
    raised=models.IntegerField()

        
    def __str__(self):
        return self.countries

class Events(models.Model):
    title=models.CharField(max_length= 50, null=False )
    content=models.TextField(max_length=400, null=False)
    date=models.DateTimeField()
    venue=models.CharField(max_length=40)