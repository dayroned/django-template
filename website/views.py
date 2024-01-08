from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import SuspiciousOperation
from django.shortcuts import redirect, resolve_url
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from .utils import recaptcha_validation

# Application Views


# Home
class HomeView(TemplateView):
    template_name = "website/home.html"


# Dashboard
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "website/dashboard.html"


# Login
class LoginView(FormView):
    template_name = "website/login.html"
    form_class = AuthenticationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recaptcha_site_key"] = settings.RECAPTCHA_SITE_KEY
        return context

    def form_valid(self, form):
        if not recaptcha_validation(self.request.POST.get("g-recaptcha-response")):
            form.add_error(None, "Invalid reCAPTCHA. Please try again.")
            return self.form_invalid(form)

        username = form.cleaned_data.get("username")
        raw_password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=raw_password)
        if not user:
            form.add_error(None, "Invalid username or password. Please try again.")
            return self.form_invalid(form)

        login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        return self.request.GET.get("next", resolve_url(settings.LOGIN_REDIRECT_URL))
