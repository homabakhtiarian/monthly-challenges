from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:month>", views.monthly_challenge_task_by_number),
    path("<str:month>", views.monthly_challenge_task, name="month-challenge"),
]
