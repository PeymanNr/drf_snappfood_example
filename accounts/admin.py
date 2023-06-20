from django.contrib import admin
from django.contrib.admin import register
from accounts.models import Customer


# Register your models here.
@register(Customer)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')

