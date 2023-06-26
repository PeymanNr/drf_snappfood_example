from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext as _
from locations.models import Address
from utils.base_models import BaseModel

User = get_user_model()


class Restaurant(BaseModel):
    user = models.OneToOneField(User, verbose_name=_('user'), on_delete=models.CASCADE)
    name = models.CharField(max_length=64, verbose_name=_('name'))
    address = models.ForeignKey(Address, verbose_name='address', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = _('restaurant')
        verbose_name_plural = _('restaurants')
        db_table = 'restaurant'

    def __str__(self):
        return self.name


class Customer(BaseModel):
    phone_regex = RegexValidator(
        regex=r'^(\+98|0)?9\d{9}$',
        message="Phone number must be entered in the format: '09...' or format: '+989..."
    )
    user = models.OneToOneField(User, verbose_name=_('user'), on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32, verbose_name=_('first_name'))
    last_name = models.CharField(max_length=32, verbose_name=_('last name'))
    phone = models.CharField(validators=[phone_regex], verbose_name="Phone Number", max_length=32)
    address = models.ForeignKey(Address, verbose_name=_('address'), on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = _('customer')
        verbose_name_plural = _('customers')
        db_table = 'customer'

    def __str__(self):
        return self.phone
