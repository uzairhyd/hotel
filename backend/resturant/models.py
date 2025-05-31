from django.db import models

# Create your models here.
class FoodCategory(models.Model):
    categoryTitle = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = 'FoodCategory'
    
    def __str__(self):
        return self.categoryTitle
    

class Food(models.Model):
    foodName = models.CharField(max_length= 100)
    foodCategory = models.ForeignKey(FoodCategory, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=500)
    price = models.FloatField()
    
    class Meta:
        verbose_name_plural = 'Food'
    
    def __str__(self):
        return self.foodName
    