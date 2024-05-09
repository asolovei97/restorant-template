from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from menu.models import DishType, Dish, Cook, User


admin.site.register(Cook)
admin.site.register(DishType)
admin.site.register(Dish)
admin.site.register(User, UserAdmin)
