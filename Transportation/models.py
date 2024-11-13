from django.db import models
from autoslug import AutoSlugField
from Storage.models import Category
from Users.models import Driver, Manager


# Create your models here.

class TransportCar(models.Model):
    license_plate = models.CharField(max_length=120)
    slug = AutoSlugField(populate_from='license_plate', unique=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    brand = models.CharField(max_length=120)
    model = models.CharField(max_length=120)
    type = models.CharField(max_length=120, choices=('trailer', 'commune', 'truck'))
    owner = models.CharField(max_length=120, choices=('company', 'driver'))
    transport_type = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.license_plate