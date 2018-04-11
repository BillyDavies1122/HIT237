from django.db import models

# Create your models here.
class customer(models.Model):
    fName = models.CharField(max_length=30, help_text="First name of customer")
    sName = models.CharField(max_length=30,help_text="Last name of customer")
    address =models.CharField(max_length=255,help_text="Address of the customer")
    phNumb = models.CharField(max_length=10,help_text="Phone number of customer")
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.fName
