from django.shortcuts import render, redirect
from .models import Adresse
from .forms import AddressForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = AddressForm(data=request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            genre = form.cleaned_data['genre']
            email = form.cleaned_data['email']
            dob = form.cleaned_data['dob']
            pays = form.cleaned_data['pays']
            region = form.cleaned_data['region']
            ville = form.cleaned_data['ville']
            profession = form.cleaned_data['profession']
            tel = form.cleaned_data['tel']
            form.save()
            return redirect('thanks')
    else:
        form = AddressForm()
    return render(request, 'core/home.html', locals())

def thanks(request):

    return render(request, 'core/thanks.html')