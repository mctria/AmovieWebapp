from django.db import models

# Create your models here.

class con_dtls(models.Model):
    
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    site = models.CharField(max_length=200,blank=True)
    msg = models.CharField(max_length=5000) 

    def __str__(self) -> str:
        return self.name

    