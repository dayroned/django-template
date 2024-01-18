from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import *


app_name = "website"

# fmt: off
urlpatterns = [
    # Home
    path("", HomeView.as_view(), name="home"),
    
    # Dashboard
    path("dashboard", DashboardView.as_view(), name="dashboard"),

    # Login
    path("login", RecaptchaLoginView.as_view(), name="login"),

    # Logout
    path("logout", LogoutView.as_view(), name="logout"),
]
# fmt: on
