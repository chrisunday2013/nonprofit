from django.db import models

from django.contrib.auth.models import User 


# home
class News_features(models.Model):
    image = models.ImageField(default="default.jpg", upload_to='portfolio_pics' )
    title=models.CharField(max_length= 50, null=False )
    subject=models.CharField(max_length=100, null=True)
    details=models.TextField(null=True)
    

        
    def __str__(self):
        return self.title

class Events(models.Model):
    title=models.CharField(max_length= 50, null=False )
    content=models.TextField(max_length=400, null=False)
    date=models.DateTimeField()
    venue=models.CharField(max_length=40)
    image = models.ImageField(default="default.jpg", upload_to='portfolio_pics' )


    def __str__(self):
        return self.title


class Team(models.Model):
    image = models.ImageField(default="default.jpg", upload_to='portfolio_pics' )
    full_name = models.CharField(max_length=100, null=False)
    position = models.CharField(max_length=50, null=False)


    def __str__(self):
        return self.full_name


class Volunteer(models.Model):
    full_name = models.CharField(max_length=100, null=False)   
    email= models.EmailField(max_length=100, null=True)  
    reason_for_joining= models.TextField(max_length=500, null=False)

    def __str__(self):
        return self.full_name


class Testimonial(models.Model):
    full_name = models.CharField(max_length=100, null=False) 
    profession = models.CharField(max_length=50, null=False)
    testimony= models.TextField(max_length=500, null=False)



class Contact(models.Model):
    full_name=models.CharField(max_length=100, null=True)
    email=models.EmailField(max_length=100, null=True)
    subject=models.CharField(max_length=100, null=True)
    message=models.TextField(null=True)

    def __str__(self):
        return self.full_name






