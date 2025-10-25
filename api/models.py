from django.db import models
from django.contrib.auth.models import User

class FoodLog(models.Model):
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='food_logs')
    
    title = models.CharField(max_length=255)
  
    serving_size = models.CharField(max_length=100)
  
    calories = models.PositiveIntegerField()
    
    MEAL_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
    ]
    
    meal_type = models.CharField(max_length=20, choices=MEAL_CHOICES)
    
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        
        return f"{self.title} ({self.meal_type}) - {self.owner}"
