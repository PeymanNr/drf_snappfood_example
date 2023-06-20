from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.admin import register
from locations.models import Address, City, Country


# Register your models here.
@register(Address)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'city')


@register(City)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@register(Country)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

