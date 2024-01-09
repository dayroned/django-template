from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import *

# Application Routes (URLs)


app_name = "website"

# fmt: off
urlpatterns = [
    # Home
    path("", HomeView.as_view(), name="home"),
    
    # Dashboard
    path("dashboard", DashboardView.as_view(), name="dashboard"),

    # Login
    path("sign-in", LoginView.as_view(), name="login"),

    # Logout
    path("sign-out", LogoutView.as_view(), name="logout"),
]
# fmt: on
