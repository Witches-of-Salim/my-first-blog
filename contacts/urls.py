from django.urls import path
from . import views
from .views import contact_list

urlpatterns = [
    path('', contact_list, name='contact_list'),
]