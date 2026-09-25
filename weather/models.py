from django.db import models
class WeatherData(models.Model):
    city=models.CharField(max_length=50)
    temperature=models.FloatField()
    description=models.CharField(max_length=20)
    humidity=models.IntegerField()
    def __str__(self):
        return self.city