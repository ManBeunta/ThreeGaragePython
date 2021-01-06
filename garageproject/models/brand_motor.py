from django.db import models
from garageproject.models.region_motor import Region_motor


class Brand_motor(models.Model):
    name = models.CharField(max_length=100)
    region_motor = models.OneToOneField(Region_motor, on_delete=models.CASCADE)

    class Meta:
        app_label = 'garageproject'

    def __str__(self):
        return f'{self.name}'