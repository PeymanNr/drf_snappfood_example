from django.db import models
from django.utils.translation import ugettext as _
from accounts.models import Customer
from restaurants.models import MenuItem, Restaurant
from utils.base_models import BaseModel


class Order(BaseModel):
    restaurant = models.ForeignKey(Restaurant, verbose_name=_('restaurant'), on_delete=models.CASCADE, related_name='orders')
    customer = models.ForeignKey(Customer, verbose_name=_('customer'), on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, verbose_name=_('menu item'), on_delete=models.CASCADE, related_name='menu_items')
    quantity = models.PositiveIntegerField(verbose_name=_('quantity'))
    total_price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=_('total price'), blank=True, null=True)

    def save(self, *args, **kwargs):
        self.total_price = self.menu_item.price * self.quantity
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('order')
        verbose_name_plural = _('orders')
        db_table = 'order'

    def __str__(self):
        return f'Order #{self.pk}'