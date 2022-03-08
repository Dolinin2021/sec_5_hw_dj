from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)


class Measurement(models.Model):
    temperature = models.FloatField()
    created_at = models.DateField(auto_now_add=True, blank=True)
    updated_at = models.DateField(auto_now=True, blank=True)
    image = models.ImageField(max_length=99999, default='')
    sensor = models.ForeignKey(Sensor, related_name='measurements', on_delete=models.CASCADE)
