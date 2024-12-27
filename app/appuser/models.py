from datetime import timezone
from django.db import models

# Create your models here.

class User (models.Model): 
    nombre_completo = models.CharField(max_length=30)       
    gmail = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    user = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()
    descripcion = models.CharField(max_length=150)

    
