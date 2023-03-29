from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from kitchen_service.forms import CookCreationForm, DishForm
from kitchen_service.models import Dish, Cook, DishType


@login_required
def index(request):
    context = {
        "num_dishes": Dish.objects.count(),
        "num_cooks": Cook.objects.count(),
        "num_dish_types": DishType.objects.count()
    }

    return render(request, "kitchen/index.html", context=context)


class CookListView(generic.ListView):
    model = Cook
    template_name = "kitchen/cook_list.html"


class CookDetailView(generic.DetailView):
    model = Cook
    template_name = "kitchen/cook_detail.html"


class CookCreateView(generic.CreateView):
    model = Cook
    form_class = CookCreationForm
    template_name = "kitchen/cook_form.html"


class DishListView(generic.ListView):
    model = Dish
    template_name = "kitchen/dish_list.html"


class DishDetailView(generic.DetailView):
    model = Dish
    template_name = "kitchen/dish_detail.html"


class DishCreateView(generic.CreateView):
    model = Dish
    form_class = DishForm
    template_name = "kitchen/dish_form.html"
    success_url = reverse_lazy("kitchen:dish-list")


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "kitchen/dish_type_list.html"
    context_object_name = "dish_type_list"
