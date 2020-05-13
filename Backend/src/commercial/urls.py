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

    CommercialInvoiceList,
    CommercialInvoiceDetail,
    CommercialInvoiceCreate,
    CommercialInvoiceUpdate,
    CommercialInvoiceDelete
    
#   QUERY
)

urlpatterns = [
    #CRUD
    path('commercial/', CommercialList.as_view()),
    path('commercial/create/', CommercialCreate.as_view()),
    path('commercial/<pk>/', CommercialDetail.as_view()),
    path('commercial/update/<pk>/', CommercialUpdate.as_view()),
    path('commercial/inactivate/<pk>/', CommercialInactivate.as_view()),
    path('commercial/delete/<pk>', CommercialDelete.as_view()),
    #QUERY
    #CRUD
    path('commercialinvoice/', CommercialInvoiceList.as_view()),
    path('commercialinvoice/create/', CommercialInvoiceCreate.as_view()),
    path('commercialinvoice/<pk>', CommercialInvoiceDetail.as_view()),
    path('commercialinvoice/update/<pk>', CommercialInvoiceUpdate.as_view()),
    path('commercialinvoice/delete/<pk>', CommercialInvoiceDelete.as_view())
    #QUERY
]
