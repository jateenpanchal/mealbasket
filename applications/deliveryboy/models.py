from django.db import models
from accounts.models import User


# Create your models here.
class Deliveryboydata(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    DeliveryBoy_Fullname = models.CharField(max_length=100)
    DeliveryBoy_PhoneNO = models.CharField(max_length=10)
    DeliveryBoy_Email = models.EmailField()
    DeliveryBoy_AdharcardNo = models.CharField(max_length=12)
    DeliveryBoy_DrivingLicenceNo = models.CharField(max_length=15)
    DeliveryBoy_PanCard = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return self.DeliveryBoy_Fullname