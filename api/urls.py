from django.urls import path
from .views import SerialNumberAPIView

urlpatterns = [
    path('check/', SerialNumberAPIView.as_view(), name='serial-check'),
]
