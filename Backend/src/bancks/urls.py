from django.urls import path

from .views import (
#   CRUDS
    BanckList,
    BanckDelete,
    BanckDetail,
    BanckCreate,
    BanckUpdate,
    BanckDelete,
    BanckInactivate
        
#   QUERY
)

urlpatterns = [
    #CRUD
    path('', BanckList.as_view()),
    path('create/', BanckCreate.as_view()),
    path('<pk>/', BanckDetail.as_view()),
    path('update/<pk>/', BanckUpdate.as_view()),
    path('inactivate/<pk>/', BanckInactivate.as_view()),
    path('delete/<pk>', BanckDelete.as_view()),
   
    #QUERY
]
