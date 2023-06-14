from django.contrib import admin
from django.contrib.admin import register
from account.models import MyUser


# Register your models here.
@register(MyUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone_number')