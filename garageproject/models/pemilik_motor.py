from django.db import models
from garageproject.models.size_motor import Size_motor
from garageproject.models.brand_motor import Brand_motor


class Pemilik_motor(models.Model):
    name = models.CharField(max_length=100)
    nameMotor = models.CharField(max_length=100)
    brand_motor = models.ForeignKey(Brand_motor, null=True, on_delete=models.SET_NULL)
    size_motor = models.ManyToManyField(Size_motor)

    class Meta:
        app_label = 'garageproject'

    def __str__(self):
        return f'{self.name}'