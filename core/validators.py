import re
from datetime import date

from django.core.exceptions import ValidationError


def validate_telephone(value):
    telNumberRegex = re.compile(r'[3,6]\d{8}')
    if re.search(telNumberRegex, value) is None :
        raise ValidationError("Enter a correct phone number ")

def validate_age(value):
    today = date.today()
    age = today.year - value.year
    if age < 18:
        raise ValidationError("You must be 18 to submit")