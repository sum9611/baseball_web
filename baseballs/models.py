from django.db import models

# Create your models here.


class test(models.Model):
    
    player_id = models.PositiveIntegerField()
    player_name = models.CharField( max_length=200)
    player_birth = models.DateTimeField()

    def __str__(self):
        return self.title