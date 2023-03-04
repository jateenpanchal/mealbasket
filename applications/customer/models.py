from django.db import models
from accounts.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Customer_Fullname = models.CharField(max_length=100)
    Customer_Email = models.EmailField()
    Customer_Phoneno = models.CharField(max_length=10)
    Customer_Address = models.TextField()
    
    def __str__(self) -> str:
        return self.Customer_Fullname
    