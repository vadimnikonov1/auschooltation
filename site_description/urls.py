from django.urls import path
from .views import home, contact

urlpatterns = [
    path('', home, name='auschool-home'),
    path('contact_form_success/', contact, name='contact_form_success')
]
