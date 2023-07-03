from django.db import models
from django.utils.translation import ugettext as _
from accounts.models import Vendor
from locations.models import Address


class Restaurant(models.Model):
    vendor = models.OneToOneField(Vendor, verbose_name=_('vendor'), on_delete=models.CASCADE)
    name = models.CharField(max_length=64, verbose_name=_('name'))
    address = models.ForeignKey(Address, max_length=128, verbose_name=_('address'), on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('restaurant')
        verbose_name_plural = _('restaurants')
        db_table = 'restaurant'


class Menu(models.Model):
    restaurant = models.OneToOneField(Restaurant, related_name='restaurant', on_delete=models.CASCADE)
    name = models.CharField(max_length=64, verbose_name=_('name'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('menu')
        verbose_name_plural = _('menus')
        db_table = 'menu'


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name='menuitems', on_delete=models.CASCADE)
    name = models.CharField(max_length=64, verbose_name=_('name'))
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=_('price'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('MenuItem')
        verbose_name_plural = _('MenuItems')
        db_table = 'MenuItem'
