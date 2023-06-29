from django.db import models
from django.utils.translation import ugettext as _
from locations.models import Address


class Restaurant(models.Model):
    name = models.CharField(max_length=64, verbose_name=_('name'))
    address = models.ForeignKey(Address, max_length=128, verbose_name=_('address'), on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name=_('restaurant'), on_delete=models.CASCADE)
    name = models.CharField(max_length=64, verbose_name=_('name'))

    def __str__(self):
        return self.name


class Food(models.Model):
    menu = models.ForeignKey(Menu, related_name='foods', on_delete=models.CASCADE)
    name = models.CharField(max_length=64, verbose_name=_('name'))
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=_('price'))

    def __str__(self):
        return self.name


#TODO: add views to show the all restaurants by city and other parameters.
# All the user authenticated or not can see the list of restaurants

