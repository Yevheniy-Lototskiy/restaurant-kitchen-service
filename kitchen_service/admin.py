from django.contrib import admin

from kitchen_service.models import Dish


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "price", "dish_type"]
    list_filter = ["dish_type"]
    search_fields = ["name"]
