from django.urls import path

from .views import (
#   CRUDS
    PaymentList,
    PaymentDelete,
    PaymentDetail,
    PaymentCreate,
    PaymentUpdate,
    PaymentDelete,

    BanckPaymentList,
    BanckPaymentDetail,
    BanckPaymentCreate,
    BanckPaymentUpdate,
    BanckPaymentDelete,
    
    DirectPaymentList,
    DirectPaymentDelete,
    DirectPaymentDetail,
    DirectPaymentCreate,
    DirectPaymentUpdate,
    
#   QUERY
    DirectPaymentReactivate,
    DirectPaymenByWorker,
    BanckPaymentByBanckList,
    PaymentByContractList
    
)

urlpatterns = [
    #CRUD
    path('payment/', PaymentList.as_view()),
    path('payment/create/', PaymentCreate.as_view()),
    path('payment/<pk>/', PaymentDetail.as_view()),
    path('payment/update/<pk>/', PaymentUpdate.as_view()),
    path('payment/delete/<pk>', PaymentDelete.as_view()),
    #QUERY
    path('payment/bycontract/<contract>', PaymentByContractList.as_view()),

    #CRUD
    path('banckpayment/', BanckPaymentList.as_view()),
    path('banckpayment/create/', BanckPaymentCreate.as_view()),
    path('banckpayment/<pk>', BanckPaymentDetail.as_view()),
    path('banckpayment/update/<pk>', BanckPaymentUpdate.as_view()),
    path('banckpayment/delete/<pk>', BanckPaymentDelete.as_view()),
    #QUERY
    path('banckpayment/bybanck/<banckPayment>', BanckPaymentByBanckList.as_view()),
    #CRUD
    path('directpayment/', DirectPaymentList.as_view()),
    path('directpayment/create/', DirectPaymentCreate.as_view()),
    path('directpayment/<pk>', DirectPaymentDetail.as_view()),
    path('directpayment/update/<pk>', DirectPaymentUpdate.as_view()),
    path('directpayment/delete/<pk>', DirectPaymentDelete.as_view()),
    #QUERY
    path('directpayment/reactivate/', DirectPaymentReactivate.as_view()),
    path('directpayment/byworker/<workerPayment>', DirectPaymenByWorker.as_view()),

]
