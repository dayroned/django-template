from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

from .utils import recaptcha_validation


class RecaptchaAuthenticationForm(AuthenticationForm):
    error_messages = {
        "invalid_login": "Invalid username or password.",
        "inactive": "This account is inactive.",
    }

    def clean(self):
        if not recaptcha_validation(self.request.POST.get("g-recaptcha-response")):
            raise ValidationError("Invalid reCAPTCHA. Please try again.")

        return super().clean()
