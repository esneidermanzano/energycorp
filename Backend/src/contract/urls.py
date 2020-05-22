from django.urls import path

from .views import (
#   CRUDS
    ContractList,
    CreateContract,
    CreateFullContract,
    GetFullContractJoin,

    InvoiceList,
    InvoiceDetail,
    InvoiceCreate,
    InvoiceUpdate,
    InvoiceDelete,
    InvoiceInactivate,    
#   QUERY

#   Generate invoices
    CreateInvoices,

#   Generate pdf
    GetInvoiceByContract,
    GeneratePdf,
#   Send email 
    SendEmail
)

urlpatterns = [
    #CRUD
    path('', InvoiceList.as_view()),
    path('create/', InvoiceCreate.as_view()),
    path('update/<pk>', InvoiceUpdate.as_view()),
    path('delete/<pk>', InvoiceDelete.as_view()),
    path('inactivate/<pk>/', InvoiceInactivate.as_view()),
    path('by-contract/', GetInvoiceByContract.as_view()),
    #QUERY
    #PDf invoice generator
    path('pdf/<contract>/<factura>/', GeneratePdf.as_view()),
    #Send invoice 
    path('sendemail/<contract>/<factura>/', SendEmail.as_view()),

    path('contract/', ContractList.as_view()),
    path('contract/create/', CreateContract.as_view()),
    path('contract-full/', GetFullContractJoin.as_view()),
    path('contract-full/create/', CreateFullContract.as_view()),

    path('generate/', CreateInvoices.as_view()),
    path('<pk>/', InvoiceDetail.as_view()),
]
