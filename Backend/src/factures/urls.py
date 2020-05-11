from django.urls import path

from .views import (
#   CRUDS
    HistoryList,
    HistoryDelete,
    HistoryDetail,
    HistoryCreate,
    HistoryUpdate,
    HistoryDelete,

    InvoiceServicesList,
    InvoiceServicesDetail,
    InvoiceServicesCreate,
    InvoiceServicesUpdate,
    InvoiceServicesDelete,
    InvoiceServicesInactivate
    
#   QUERY
)

urlpatterns = [
    #CRUD
    path('history/', HistoryList.as_view()),
    path('history/create/', HistoryCreate.as_view()),
    path('history/<pk>/', HistoryDetail.as_view()),
    path('history/update/<pk>/', HistoryUpdate.as_view()),
    path('history/delete/<pk>', HistoryDelete.as_view()),
    #QUERY
    #CRUD
    path('invoiceservices/', InvoiceServicesList.as_view()),
    path('invoiceservices/create/', InvoiceServicesCreate.as_view()),
    path('invoiceservices/<pk>', InvoiceServicesDetail.as_view()),
    path('invoiceservices/update/<pk>', InvoiceServicesUpdate.as_view()),
    path('invoiceservices/delete/<pk>', InvoiceServicesDelete.as_view()),
    path('invoiceservices/inactivate/<pk>/', InvoiceServicesInactivate.as_view()),
    #QUERY
]
