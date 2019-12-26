"""
validators.py is just a file to validate the forms.py

"""
import re
from datetime import date

from django.core.exceptions import ValidationError

from .models import Adresse


def validate_telephone(value):
    telNumberRegex = re.compile(r'[3,6]\d{8}')
    if re.search(telNumberRegex, value) is None :
        raise ValidationError("Enter a correct phone number ")
    elif Adresse.objects.filter(tel=value).exists():
        raise ValidationError("This number exist already! ")

def validate_age(value):
    today = date.today()
    age = today.year - value.year
    if age < 18:
        raise ValidationError("You must be 18 to submit")