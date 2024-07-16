from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView

from .forms import ReCaptchaAuthenticationForm


# Home
class HomeView(TemplateView):
    template_name = "website/home.html"


# Dashboard
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "website/dashboard.html"


# Login
class ReCaptchaLoginView(LoginView):
    template_name = "website/login.html"
    form_class = ReCaptchaAuthenticationForm
