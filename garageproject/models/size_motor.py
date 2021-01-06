from django.db import models


class Size_motor(models.Model):
    name = models.CharField(max_length=100)
    beratMotor = models.FloatField()

    class Meta:
        app_label = 'garageproject'

    def __str__(self):
        return f'{self.name} ({self.beratMotor})'