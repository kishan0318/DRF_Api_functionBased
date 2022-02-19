from django.db import models

# Create your models here.
class Items(models.Model):
    P_name=models.CharField(max_length=255)
    P_details=models.CharField(max_length=255)
    P_qty=models.IntegerField()
    P_price=models.IntegerField()
    
    def __str__(self):
        return self.P_name
