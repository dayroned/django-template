from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import SuspiciousOperation
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView

from .utils import recaptcha_validation

# Application Views


# Home Page
class HomePageView(TemplateView):
    template_name = "website/home_page.html"


# Profile Page
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "website/dashboard.html"


# Login Page
def login_page(request):
    if request.method == "POST":
        if recaptcha_validation(request.POST.get("g-recaptcha-response")):
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                raw_password = form.cleaned_data.get("password")
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                next_page = request.GET.get("next", settings.LOGIN_REDIRECT_URL)
                return redirect(next_page)
        else:
            raise SuspiciousOperation()
    else:
        form = AuthenticationForm()

    context = {"form": form, "recaptcha_site_key": settings.RECAPTCHA_SITE_KEY}
    return render(request, "website/login_page.html", context)
