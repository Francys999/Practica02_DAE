from django.db import models

class Athlete(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    sport = models.CharField(max_length=50)
    achievements = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='athletes/', blank=True)

    def __str__(self):
        return self.name
