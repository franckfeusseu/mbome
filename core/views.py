from django.shortcuts import render, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (CreateView, FormView)

from .models import Adresse
from .forms import AddressForm


# Create your views here.
class NewAdresseView(SuccessMessageMixin, CreateView):
    model = Adresse
    form_class = AddressForm
    success_url = reverse_lazy('core:thanks')
    template_name = 'core/home.html'
    success_message = "Thanks your data was saved"

def thanks(request):
    return render(request, 'core/thanks.html')


def privacy_policy(request):
    return render(request, 'core/privacy_policy.html')


def tos(request):
    return render(request, 'core/tos.html')
