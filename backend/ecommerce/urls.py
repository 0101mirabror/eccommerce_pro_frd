from django.urls import path
from .apiviews import ObtainTokenView

urlpatterns = [
    # Other URL patterns
    path('token/', ObtainTokenView.as_view(), name='obtain-token'),
]