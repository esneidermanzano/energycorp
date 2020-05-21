from django.urls import path

from .views import (
    MoraAndSuspended,
    TopFiveCounters
)

urlpatterns = [
    path('moraandsuspended/',MoraAndSuspended.as_view()),
    path('topfive/',TopFiveCounters.as_view())
]

