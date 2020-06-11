from django.urls import path

# from .views import purchase
from .views import CarpetImageClassifierAPIView

urlpatterns = [
    path('image/', CarpetImageClassifierAPIView.as_view(), name='carpet-image-classifier')
]