from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register/", views.SignUp, name="sign-up"),
    path("sign-in/", views.SignIn, name="sign-in"),
    path("sign-out/", auth_views.LogoutView.as_view(template_name="users/signout.html"), name="sign-out"),
    path("profile/", views.profile, name="profile"),
]
