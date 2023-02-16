from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home-page"),
    path("donate-now/", views.donate, name="donation-page"),
    path("success/<str:args>", views.success, name="success-page"),
]
