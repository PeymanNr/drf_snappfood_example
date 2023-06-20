from django.db import models
from django.utils.translation import ugettext as _

from utils.base_models import BaseModel


class Country(BaseModel):
    name = models.CharField(max_length=32, verbose_name=_('country'))

    # TODO: add meta class
    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')
        db_table = 'Countries'
    # TODO: add __str__

    def __str__(self):
        return self.name


class City(BaseModel):
    name = models.CharField(max_length=32, verbose_name=_('city'))
    country = models.ForeignKey(Country, verbose_name=_('country'), related_name='cities', on_delete=models.CASCADE)

    # TODO : add meta class
    class Meta:
        verbose_name = _('City')
        verbose_name_plural = _('Cities')
        db_table = 'Cities'
    # TODO: add __str__

    def __str__(self):
        return self.name


class Address(BaseModel):
    city = models.ForeignKey(City, verbose_name=_('city'), related_name='addresses', on_delete=models.CASCADE)
    description = models.TextField(max_length=500, verbose_name='description')

    # TODO: add meta class
    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')
        db_table = 'Addresses'
