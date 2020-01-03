from django.shortcuts import render, redirect

from .forms import AddressForm


# Create your views here.

def create_address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save()
            return redirect("https://www.djangoproject.com")
    else:
        form = AddressForm()
    return render(request,
                  'core/home.html',
                  {'form': form}
                  )



def privacy_policy(request):
    return render(request, 'core/privacy_policy.html')


def tos(request):
    return render(request, 'core/tos.html')
