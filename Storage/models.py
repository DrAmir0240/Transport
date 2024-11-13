from django.db import models
from autoslug import AutoSlugField

from Users.models import Customer, Manager


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(populate_from='name', unique=True)
    picture = models.ImageField(upload_to='category_pictures')
    vulnerability = models.CharField(max_length=100, choices=('very_vulnerable', 'high', 'medium', 'no need to worry'))
    description = models.TextField()

    def __str__(self):
        return self.name


class Cargo(models.Model):
    cargo_id = models.CharField(max_length=100, unique=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    date_added = models.DateField(auto_now_add=True)
    picture = models.ImageField(upload_to='cargo_pictures')

    def generate_cargo_id(self):
        return f'{self.date_added}-{self.owner.id}-{self.manager.id}-{self.category.id}'

    def __str__(self):
        return self.cargo_id
