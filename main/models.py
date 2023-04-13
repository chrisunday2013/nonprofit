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
    


   


class Donate(models.Model):
    PAYMENT_CHOICES = [
        ('paypal', 'PayPal'),
        ('payStack', 'PayStack'),
    ]

    AMOUNT_CHOICES = [
        ('25', '25'),
        ('50', '50'),
        ('75', '75'),
        ('100', '100'),
    ]

    amount=models.CharField(max_length=100, choices=AMOUNT_CHOICES, default='25')
    full_name=models.CharField(max_length=100, null=True)
    email=models.EmailField(max_length=100, null=True)
    message=models.TextField(null=True)
    payment=models.CharField(max_length=100, choices=PAYMENT_CHOICES, default='paypal')
    

    def __str__(self):
        return self.amount    
    
    
class FAQ(models.Model):
    question=models.CharField(max_length=300)    
    answer=models.TextField()

    def __str__(self):
        return self.question






