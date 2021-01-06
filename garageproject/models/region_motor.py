from django.db import models


class Region_motor(models.Model):
    """ pemilik unique region """
    name = models.CharField(max_length=100)

    class Meta:
        app_label = 'garageproject'

    def __str__(self):
        return f'{self.name}'