from django.urls import path

from .views import (

    Login,
    UserList, 
    UserDetail,
    UserCreate, 
    UserUpdate,
    DeleteUser,

    ClientList, 
    ClientDetail,
    ClientCreate,
    NewClientCreate,
    ClientUpdate,
    DeleteClient,

    WorkerList,
    WorkerDetail,
    CreateWorker,
    NewWorkerCreate,
    WorkerUpdate,
    DeleteWorker
)


urlpatterns = [

    path('', UserList.as_view()),
    path('login/', Login.as_view()),
    path('create/', UserCreate.as_view()),
    path('client/', ClientList.as_view()),
    path('client/create/', ClientCreate.as_view()),
    path('client/create-new/', NewClientCreate.as_view()),
    path('client/<pk>/', ClientDetail.as_view()),
    path('client/<pk>/update/', ClientUpdate.as_view()),
    path('client/<pk>/delete/', DeleteClient.as_view()),
    path('worker/', WorkerList.as_view()),
    path('worker/create/', CreateWorker.as_view()),
    path('worker/create-new/', NewWorkerCreate.as_view()),
    path('worker/<pk>', WorkerDetail.as_view()),
    path('worker/<pk>/update', WorkerUpdate.as_view()),
    path('worker/<pk>/delete', DeleteWorker.as_view()),
    path('<pk>/', UserDetail.as_view()),
    path('<pk>/update/', UserUpdate.as_view()),
    path('<pk>/delete/', DeleteUser.as_view())
]