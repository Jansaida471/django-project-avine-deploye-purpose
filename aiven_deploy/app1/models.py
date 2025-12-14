from django.db import models

# Create your models here.
class  users(models.Model):
    user_id=models.CharField(max_length=150)
    user_gender=models.CharField(max_length=100)
    user_email=models.EmailField(unique=True)
    
