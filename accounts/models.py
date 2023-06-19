from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext as _

from locations.models import Address
from utils.base_models import BaseModel

User = get_user_model()


class Restaurant(BaseModel):
    user = models.OneToOneField(User, verbose_name=_('user'), on_delete=models.CASCADE)
    name = models.CharField(max_length=64, verbose_name=_('name'))
    address = models.ForeignKey(Address, verbose_name='address', on_delete=models.SET_NULL, null=True)

    # TODO: add meta class
    # TODO: add __str__


class Customer(BaseModel):
    user = models.OneToOneField(User, verbose_name=_('user'), on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32, verbose_name=_('first_name'))
    last_name = models.CharField(max_length=32, verbose_name=_('last name'))
    # TODO: add validator to validate the phone number of user
    phone = models.CharField(max_length=32)
    address = models.ForeignKey(Address, verbose_name=_('address'), on_delete=models.SET_NULL, null=True)

    # TODO: add meta class
    # TODO: add __str__
