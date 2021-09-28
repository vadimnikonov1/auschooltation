from django.urls import path
from .views import register_or_log_in

urlpatterns = [
    path('', register_or_log_in, name='registration_and_login'),
]
