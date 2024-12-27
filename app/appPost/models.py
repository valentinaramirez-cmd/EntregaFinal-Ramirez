from django.db import models
from datetime import datetime

# Create your models here.

class Post (models.Model): 
    fecha = models.DateTimeField(auto_now_add=True)
    tit= models.CharField(max_length=20)
    texto = models.TextField()
    user = models.CharField(max_length=20)
    ##imagen/es 



