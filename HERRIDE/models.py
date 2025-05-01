from django.db import models

class CustomUser(models.Model):
    uphn = models.CharField(max_length=10, primary_key=True)  # Phone as String
    uname = models.CharField(max_length=20)  # User name should be CharField
    uemail = models.EmailField(max_length=50, unique=True)  # Unique email
    uadd = models.CharField(max_length=50)  # Address should be CharField
    upwd = models.CharField(max_length=128)  # Store hashed password

    def __str__(self):
        return self.uname  # Display name in admin panel
    
class Driver(models.Model):
    dphn=models.CharField(max_length=10,primary_key=True)
    dname=models.CharField(max_length=20)
    demail=models.EmailField(max_length=30,unique=True)
    dadd=models.CharField(max_length=50)
    dpwd=models.CharField(max_length=128)

    def __str__(self):
        return self.dname  # Display name in admin panel
    

