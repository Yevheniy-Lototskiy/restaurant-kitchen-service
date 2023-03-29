from django.urls import path

from kitchen_service.views import (
    index,
    CookListView,
    CookDetailView,
    CookCreateView,
    DishListView,
    DishDetailView,
    DishCreateView,
    DishTypeListView,
    DishTypeCreateView,
)

urlpatterns = [
    path("", index, name="index"),

    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),

    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),

    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("dish-types/create/", DishTypeCreateView.as_view(), name="dish-type-create")
]

app_name = "kitchen"
