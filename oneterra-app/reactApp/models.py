from django.db import models

# Create your models here.

class AppSettings(models.Model):
    name = models.CharField(max_length=150)
    title = models.CharField(max_length=150, blank=True)
    description = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name
    
