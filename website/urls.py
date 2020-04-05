from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import *

# Application Routes (URLs)


app_name = "website"

# fmt: off
urlpatterns = [
    # Home Page
    path("", HomePageView.as_view(), name="home_page"),
    
    # Dashboard
    path("dashboard", DashboardView.as_view(), name="dashboard"),

    # Login
    path("auth/login", login_page, name="login"),

    # Logout
    path("auth/logout", LogoutView.as_view(), name="logout"),
]
# fmt: on
