from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import SuspiciousOperation
from django.shortcuts import render, redirect

from .utils import recaptcha_validation

# Application Views


# Login
def core_login(request):
    if (request.method == 'POST'):
        if recaptcha_validation(request.POST.get('g-recaptcha-response')):
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                next_page = request.GET.get('next', settings.LOGIN_REDIRECT_URL)
                return redirect(next_page)
        else:
            raise SuspiciousOperation()
    else:
        form = AuthenticationForm()

    context = {'form': form, 'recaptcha_site_key': settings.RECAPTCHA_SITE_KEY}
    return render(request, 'registration/login_page.html', context)

# 2020.04.01-DEA
