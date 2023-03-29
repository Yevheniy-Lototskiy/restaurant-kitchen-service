from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from kitchen_service.models import Dish, Cook, DishType


@login_required
def index(request):

    context = {
        "num_dishes": Dish.objects.count(),
        "num_cooks": Cook.objects.count(),
        "num_dish_types": DishType.objects.all()
    }

    return render(request, "kitchen/index.html", context=context)
