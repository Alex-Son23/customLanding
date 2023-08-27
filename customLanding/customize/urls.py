from django.urls import path
from .views import index, form_view

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('form/', form_view, name='form')
]