from django.urls import path

from .views import (
#   CRUDS
    InvoiceServicesList,
    InvoiceServicesDetail,
    InvoiceServicesCreate,
    InvoiceServicesUpdate,
    InvoiceServicesDelete,
    InvoiceServicesInactivate,    
#   QUERY

#   Generate pdf
    GeneratePdf
)

urlpatterns = [
    #CRUD
    path('invoiceservices/', InvoiceServicesList.as_view()),
    path('invoiceservices/create/', InvoiceServicesCreate.as_view()),
    path('invoiceservices/<pk>', InvoiceServicesDetail.as_view()),
    path('invoiceservices/update/<pk>', InvoiceServicesUpdate.as_view()),
    path('invoiceservices/delete/<pk>', InvoiceServicesDelete.as_view()),
    path('invoiceservices/inactivate/<pk>/', InvoiceServicesInactivate.as_view()),
    #QUERY
    #PDf invoice generator
    path('pdf/', GeneratePdf.as_view()),
]
