from ast import Try
from pyexpat import model
from django.db import models

# Create your models here.

class Reservation(models.Model):
  
  customerName=models.CharField(max_length=50,null=True)
  customerMobile=models.CharField(max_length=20,null=True)
  hall=models.CharField(max_length=20,null=True)
  peopleNumber=models.IntegerField(null=True)
  date=models.CharField(max_length=20,null=True)
  status=models.CharField(max_length=20,null=True,default="pending")
  
  def __str__(self):
    return f"{self.customerName} - {self.hall} - {self.date}"
  