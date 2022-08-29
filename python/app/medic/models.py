from django.db import models

# Create your models here.

class Patient(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    taxNumber = models.CharField(max_length=100, blank=True, default='')
    registrationNumber = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.name