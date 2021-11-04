from django.urls import path
from django.urls.resolvers import URLPattern
from .views import MutantView


urlpatterns = [
    path('mutant/', MutantView.as_view(), name='mutantData'),
]