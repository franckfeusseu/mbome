from datetime import date
import re

from django import forms
from django.core.exceptions import ValidationError

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from .models import Adresse

SEX = (
    ('', 'Choose...'),
    ('Male', 'Male'),
    ('Female', 'Female')
)

REGION = (
    ('', 'Choose...'),
    ('Adamaoua', 'Adamaoua'),
    ('Centre', 'Centre'),
    ('Est', 'Est'),
    ('Extreme-Nord', 'Extreme-Nord'),
    ('Littoral', 'Littoral'),
    ('Nord', 'Nord'),
    ('Nord-Ouest', 'Nord-Ouest'),
    ('Ouest', 'Ouest'),
    ('Sud', 'Sud'),
    ('Sud-Ouest', 'Sud-Ouest')
)

PAYS = (
    ('', 'Choose....'),
    ('CMR', 'Cameroun')
)

PROFESSION = (
    ('AGR', 'Agriculteur'),
    ('ETU', 'Etudiant'),
    ('MEN', 'Menagere'),
    ('OUV', 'Ouvrier')
)

class DateInput(forms.DateInput):
    input_type = 'date'

class AddressForm(forms.Form):
    nom = forms.CharField()
    prenom = forms.CharField()
    genre = forms.ChoiceField(choices=SEX)
    email = forms.EmailField()
    dob = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    pays = forms.ChoiceField(choices=PAYS)
    region = forms.ChoiceField(choices=REGION)
    ville = forms.CharField()
    profession = forms.ChoiceField(choices=PROFESSION)
    tel = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('nom', css_class='form-group col-md-6 mb-0'),
                Column('prenom', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'genre',
            'dob',
            'email',
            'pays',
            'region',
            'ville',
            'profession',
            'tel',
            Submit('submit', 'Submit')
        )

    def clean_dob(self):
        dob = self.cleaned_data['dob']
        today = date.today()
        age = today.year - dob.year
        if age < 18:
            raise ValidationError("You must be 18 to submit")

    def clean_tel(self):
        tel = self.cleaned_data['tel']
        telNumberRegex = re.compile(r'[3,6]\d{8}')
        if re.search(telNumberRegex, tel) is None :
            raise ValidationError("Enter a correct phone number ")



    def save(self):
        cleaned_data = self.cleaned_data
        Adresse.objects.create(
            nom=cleaned_data["nom"],
            prenom=cleaned_data["prenom"],
            genre=cleaned_data["genre"],
            email=cleaned_data["email"],
            dob=cleaned_data["dob"],
            pays=cleaned_data["pays"],
            region=cleaned_data["region"],
            ville=cleaned_data["ville"],
            profession=cleaned_data["profession"],
            tel=cleaned_data["tel"]
        )