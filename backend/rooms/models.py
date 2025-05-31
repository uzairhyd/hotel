from django.db import models

# Create your models here.

class RoomTypes(models.Model):
    typeName = models.CharField(max_length=50)
    roomDescription = models.CharField(max_length=200)
    costPerNight = models.FloatField()
    discount_percent = models.FloatField()
    
    class Meta:
        verbose_name_plural = 'RoomTypes'
    
    def __str__(self):
        return self.typeName
    