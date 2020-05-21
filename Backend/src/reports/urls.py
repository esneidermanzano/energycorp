from django.urls import path

from .views import (
    MoraAndSuspended,
    TopFiveCounters,
     QuantityCounterTransformator
)

urlpatterns = [
    path('moraandsuspended/',MoraAndSuspended.as_view()),
    path('topfive/',TopFiveCounters.as_view()),
    path('quantitycounterfortransformator/', QuantityCounterTransformator.as_view())
]

