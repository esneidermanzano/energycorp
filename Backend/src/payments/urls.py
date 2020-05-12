from django.urls import path

from .views import (
#   CRUDS
    PaymentList,
    PaymentDelete,
    PaymentDetail,
    PaymentCreate,
    PaymentUpdate,
    PaymentDelete,
    PaymentInactivate,

    BanckPaymentList,
    BanckPaymentDetail,
    BanckPaymentCreate,
    BanckPaymentUpdate,
    BanckPaymentDelete,
    BanckPaymentInactivate,
    
    DirectPaymentList,
    DirectPaymentDelete,
    DirectPaymentDetail,
    DirectPaymentCreate,
    DirectPaymentUpdate,
    DirectPaymentInactivate
    
#   QUERY
)

urlpatterns = [
    #CRUD
    path('payment/', PaymentList.as_view()),
    path('payment/create/', PaymentCreate.as_view()),
    path('payment/<pk>/', PaymentDetail.as_view()),
    path('payment/update/<pk>/', PaymentUpdate.as_view()),
    path('payment/inactivate/<pk>/', PaymentInactivate.as_view()),
    path('payment/delete/<pk>', PaymentDelete.as_view()),
    #QUERY
    #CRUD
    path('banckpayment/', BanckPaymentList.as_view()),
    path('banckpayment/create/', BanckPaymentCreate.as_view()),
    path('banckpayment/<pk>', BanckPaymentDetail.as_view()),
    path('banckpayment/update/<pk>', BanckPaymentUpdate.as_view()),
    path('banckpayment/delete/<pk>', BanckPaymentDelete.as_view()),
    path('banckpayment/inactivate/<pk>/', BanckPaymentInactivate.as_view()),
    #QUERY
    #CRUD
    path('directpayment/', DirectPaymentList.as_view()),
    path('directpayment/create/', DirectPaymentCreate.as_view()),
    path('directpayment/<pk>', DirectPaymentDetail.as_view()),
    path('directpayment/update/<pk>', DirectPaymentUpdate.as_view()),
    path('directpayment/delete/<pk>', DirectPaymentDelete.as_view()),
    path('directpayment/inactivate/<pk>/', DirectPaymentInactivate.as_view())
    #QUERY
]
