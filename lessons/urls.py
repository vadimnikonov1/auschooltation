from django.urls import path
from .views import heart_basics, heart_norm

urlpatterns = [
    path('heart_basics/', heart_basics, name='heart_basics'),
    path('heart_norm/', heart_norm, name='heart_norm'),
]
