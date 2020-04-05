from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import *

# Application Routes (URLs)


app_name = 'core'

urlpatterns = [

    # Login
    path('auth/login', core_login, name='login'),

    # Logout
    path('auth/logout', LogoutView.as_view(), name='logout'),
]

# 2020.04.01-DEA
