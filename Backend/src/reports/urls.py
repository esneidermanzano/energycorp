from django.urls import path

from .views import (
    MoraAndSuspended
)

urlpatterns = [
    path('moraandsuspended/',MoraAndSuspended.as_view())
]
