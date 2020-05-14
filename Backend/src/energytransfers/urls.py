from django.urls import path

from .views import (
#   CRUDS
    SubstationList,
    SubstationDelete,
    SubstationDetail,
    SubstationCreate,
    SubstationUpdate,
    SubstationDelete,
    SubstationInactivate,

    TransformatorList,
    TransformatorDetail,
    TransformatorCreate,
    TransformatorUpdate,
    TransformatorDelete,
    TransformatorInactivate,
    
    CounterList,
    CounterDelete,
    CounterDetail,
    CounterCreate,
    CounterUpdate,
    CounterInactivate,

    HistoryList,
    HistoryDelete,
    HistoryDetail,
    HistoryCreate,
    HistoryUpdate,
    HistoryDelete
    
#   QUERY
)

urlpatterns = [
    #CRUD
    path('substation/', SubstationList.as_view()),
    path('substation/create/', SubstationCreate.as_view()),
    path('substation/<pk>/', SubstationDetail.as_view()),
    path('substation/update/<pk>/', SubstationUpdate.as_view()),
    path('substation/inactivate/<pk>/', SubstationInactivate.as_view()),
    path('substation/delete/<pk>', SubstationDelete.as_view()),
    #QUERY
    #CRUD
    path('transformator/', TransformatorList.as_view()),
    path('transformator/create/', TransformatorCreate.as_view()),
    path('transformator/<pk>', TransformatorDetail.as_view()),
    path('transformator/update/<pk>', TransformatorUpdate.as_view()),
    path('transformator/delete/<pk>', TransformatorDelete.as_view()),
    path('transformator/inactivate/<pk>/', TransformatorInactivate.as_view()),
    #QUERY
    #CRUD
    path('counter/', CounterList.as_view()),
    path('counter/create/', CounterCreate.as_view()),
    path('counter/<pk>', CounterDetail.as_view()),
    path('counter/update/<pk>', CounterUpdate.as_view()),
    path('counter/delete/<pk>', CounterDelete.as_view()),
    path('counter/inactivate/<pk>/', CounterInactivate.as_view()),
    #QUERY
        #CRUD
    path('history/', HistoryList.as_view()),
    path('history/create/', HistoryCreate.as_view()),
    path('history/<pk>/', HistoryDetail.as_view()),
    path('history/update/<pk>/', HistoryUpdate.as_view()),
    path('history/delete/<pk>', HistoryDelete.as_view()),
    #QUERY
]
