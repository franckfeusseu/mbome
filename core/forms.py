import re


from django import forms
from django.forms import ModelForm


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

from .models import Adresse
from .validators import validate_age, validate_telephone


class AddressForm(ModelForm):
    check_me_out = forms.BooleanField(
        label=('I agree to the terms and conditions and privacy policy'),
        required=True,
        error_messages={'required': 'please tick the box'}
    )
    dob = forms.DateField(required=True, validators=[validate_age])
    tel = forms.CharField(required=True, validators=[validate_telephone])

    def __init__(self, *args, **kwargs):
        super(AddressForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
             Row(
                Column('nom', css_class='form-group col-md-6 mb-0'),
                Column('prenom', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('genre', css_class='form-group col-md-6 mb-0'),
                Column('dob', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'email',
            Row(
                Column('pays', css_class='form-group col-md-6 mb-0'),
                Column('region', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('ville', css_class='form-group col-md-6 mb-0'),
                Column('profession', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'tel',
            'check_me_out',
            Submit('submit', 'Submit'))

    class Meta:
        model = Adresse
        fields = '__all__'