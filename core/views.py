from django.shortcuts import render, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (CreateView)
from django.http import JsonResponse

from .models import Adresse
from .forms import AddressForm


# Create your views here.
class NewAdresseView(CreateView):
    model = Adresse
    form_class = AddressForm
    success_url = reverse_lazy('core:thanks')
    template_name = 'core/home.html'


def thanks(request):
    return render(request, 'core/thanks.html')

#def validate_nom(request):
#   nom = request.GET.get('nom', None)
#   data = {
#      'is_taken': Adresse.objects.filter(nom_iexact=nom).exists()
#    }
#    if data['is_taken']:
#        data['error_message'] = 'A user with this username already exits.'
#    return JsonResponse(data)


def privacy_policy(request):
    return render(request, 'core/privacy_policy.html')


def tos(request):
    return render(request, 'core/tos.html')
