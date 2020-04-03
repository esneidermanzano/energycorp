from django.urls import path

from .views import (

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
    TransformatorInactivate
)



urlpatterns = [
    path('substation/', SubstationList.as_view()),
    path('substation/create/', SubstationCreate.as_view()),
    path('substation/<pk>/', SubstationDetail.as_view()),
    path('substation/update/<pk>/', SubstationUpdate.as_view()),
    path('substation/inactivate/<pk>/', SubstationInactivate.as_view()),
    path('substation/delete/<pk>', SubstationDelete.as_view()),
    path('transformator/', TransformatorList.as_view()),
    path('transformator/create/', TransformatorCreate.as_view()),
    path('transformator/<pk>', TransformatorDetail.as_view()),
    path('transformator/update/<pk>', TransformatorUpdate.as_view()),
    path('transformator/delete/<pk>', TransformatorDelete.as_view()),
    path('transformator/inactivate/<pk>/', TransformatorInactivate.as_view())

]
