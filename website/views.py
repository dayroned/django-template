from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView
from django.shortcuts import render

from .forms import RecaptchaAuthenticationForm


# Home
class HomeView(TemplateView):
    template_name = "website/home.html"

    def get(self, request, *args, **kwargs):
        if "HX-Request" in request.headers:
            print("HX-Request")
            return render(request, "website/home_content.html")
        return super().get(request, *args, **kwargs)


# Dashboard
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "website/dashboard.html"

    def get(self, request, *args, **kwargs):
        if "HX-Request" in request.headers:
            print("HX-Request")
            return render(request, "website/dashboard_content.html")
        return super().get(request, *args, **kwargs)


# Login
class RecaptchaLoginView(LoginView):
    template_name = "website/login.html"
    form_class = RecaptchaAuthenticationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recaptcha_site_key"] = settings.RECAPTCHA_SITE_KEY
        return context
