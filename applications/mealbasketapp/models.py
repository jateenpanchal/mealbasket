from django.db import models

# Create your models here.
class category(models.Model):
    category_name = models.CharField(max_length=50)
    category_pic = models.ImageField(upload_to='img/category_picture/')
    category_status = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.category_name