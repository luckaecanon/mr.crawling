from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/detail/", views.index, name="detail"),
    path("<int:question_id>/detail/", views.index, name="detail"),
    path("<int:question_id>/vote/", views.index, name="vote")

]