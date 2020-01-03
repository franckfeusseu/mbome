from django.urls import path
from django.views.generic.base import RedirectView
from . import views

app_name = 'core'
urlpatterns = [
#    path('', views.NewAdresseView.as_view(), name='register'),
    path('', views.create_address, name='register'),
    path('thanks', RedirectView.as_view(url='https://data-flair.training/blogs/django-redirect/')),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),
    path('terms_of_service', views.tos, name='tos'),
#    path('validate_nom', views.validate_nom, name='validate_nom'),
]