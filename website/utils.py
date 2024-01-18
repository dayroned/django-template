import requests

from django.conf import settings


# Adapted from: https://simpleisbetterthancomplex.com/tutorial/2017/02/21/how-to-add-recaptcha-to-django-site.html
# Validates reCAPTCHA
def recaptcha_validation(recaptcha_response):
    """Begin reCAPTCHA validation"""
    data = {"secret": settings.RECAPTCHA_SECRET_KEY, "response": recaptcha_response}
    r = requests.post("https://www.google.com/recaptcha/api/siteverify", data=data)
    result = r.json()
    """ End reCAPTCHA validation """

    if result["success"]:
        return True

    return False
