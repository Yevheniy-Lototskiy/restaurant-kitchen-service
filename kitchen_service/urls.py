from django.urls import path

from kitchen_service.views import index

urlpatterns = [
    path("", index, name="index"),
]

app_name = "kitchen"
