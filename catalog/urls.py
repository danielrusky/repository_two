from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import index, contact, trevor, base, artur, artur_two

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('trevor/', trevor, name='trevor'),
    path('base/', base, name='base'),
    path('artur/', artur, name='artur'),
    path('artur_two/', artur_two, name='artur_two'),
]