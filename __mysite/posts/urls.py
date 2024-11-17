from django.contrib import admin
from django.urls import include, path
from . import views



urlpatterns = [
    path('ass/', views.aaaaa),
    path('home/', views.home, name="home"),
    # PATH CONVENTION
    path("<int:id>", views.post)
]