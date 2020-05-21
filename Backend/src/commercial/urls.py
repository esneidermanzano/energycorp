from django.urls import path

from .views import (
#   CRUDS
    CommercialList,
    CommercialDelete,
    CommercialDetail,
    CommercialCreate,
    CommercialUpdate,
    CommercialDelete,
    CommercialInactivate,

#   QUERY
)

urlpatterns = [
    #CRUD
    path('', CommercialList.as_view()),
    path('create/', CommercialCreate.as_view()),
    path('<pk>/', CommercialDetail.as_view()),
    path('update/<pk>/', CommercialUpdate.as_view()),
    path('inactivate/<pk>/', CommercialInactivate.as_view()),
    path('delete/<pk>', CommercialDelete.as_view())
    #QUERY
]
