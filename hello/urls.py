from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name= "index"),
    path("floki", views.floki, name= "floki"),
    path("valorant", views.valorant, name= "valorant"),
    path("<str:name>", views.greet, name="great")

]