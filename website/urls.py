from django.urls import path

from .views import *

# Application Routes (URLs)


app_name = 'website'

urlpatterns = [

    # Home Page
    path('', HomePageView.as_view(), name='home_page'),

    # Dashboard
    path('dashboard', DashboardView.as_view(), name='dashboard'),
]
