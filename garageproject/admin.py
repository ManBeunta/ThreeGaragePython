from django.contrib import admin
from garageproject.models.brand_motor import Brand_motor
from garageproject.models.pemilik_motor import Pemilik_motor
from garageproject.models.region_motor import Region_motor
from garageproject.models.size_motor    import Size_motor

# Register your models here.
admin.site.register(Brand_motor)
admin.site.register(Pemilik_motor)
admin.site.register(Region_motor)
admin.site.register(Size_motor)