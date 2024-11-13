from django.db import models
from django.db.models import CharField, Choices

from Storage.models import Cargo
from Transportation.models import TransportCar
from Users.models import Driver, Manager


# Create your models here.

class Order(models.Model):
    cargo = models.OneToOneField(Cargo, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    car = models.ForeignKey(TransportCar, on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    send_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    storage_period = models.IntegerField()  # days of storage
    transport_distance = models.DecimalField(max_digits=20, decimal_places=2)
    transport_range = models.CharField(max_length=50, choices=('International', 'Interior', 'Intrastate'))

    def __str__(self):
        return f"{self.cargo}"


class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=('Cash', 'Online', 'Cryptocurrency'))

    def __str__(self):
        return self.order.id