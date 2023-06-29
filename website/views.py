from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as AuthLoginView
from django.shortcuts import resolve_url
from django.views.generic.base import TemplateView

from .forms import RecaptchaAuthenticationForm

# Application Views


# Home
class HomeView(TemplateView):
    template_name = "website/home.html"


# Dashboard
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "website/dashboard.html"


# Login
class LoginView(AuthLoginView):
    template_name = "website/login.html"
    form_class = RecaptchaAuthenticationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recaptcha_site_key"] = settings.RECAPTCHA_SITE_KEY
        return context
