from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('', views.NewAdresseView.as_view(), name='register'),
    path('thanks', views.thanks, name='thanks'),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),
    path('terms_of_service', views.tos, name='tos'),
#    path('validate_nom', views.validate_nom, name='validate_nom'),
]