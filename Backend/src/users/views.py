from rest_framework.generics import (
    ListAPIView, 
    RetrieveAPIView, 
    ListCreateAPIView, 
    RetrieveAPIView, 
    UpdateAPIView,
    DestroyAPIView
)
from rest_framework.permissions import IsAdminUser, BasePermission

from users.models import CustomUser, Client, Worker


from users.serializers import (
    UserSerializer, 
    UpdateUserSerializer,
    CreateUserSerializer, 
    CreateNewClientSerializer,
    ClientSerializer, 
    CreateClientSerializer,
    UpdateClientSerializer,
    WorkerSerializer,
    CreateNewWorkerSerializer
)
from rest_framework.views import APIView 
from rest_framework.response import Response

from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

class AllowAn(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            quey = Worker.objects.filter(user=request.user.id).values('user_type')
            return bool(quey[0]['user_type']==3)            
        else:
            return False

class Login(APIView):
  def post(self,request):
    id_user = request.data.get('id_user',None)
    password = request.data.get('password',None)
    if id_user and password:
        user_querysets = Worker.objects.filter(user__id_user__iexact= id_user ).values('id','user','user__id_user', 'user__is_active',  'user__password', 'user_type')  
        if (user_querysets.exists() and  user_querysets[0]['user__is_active']) :
            user= user_querysets[0]
            if(check_password(password, user['user__password'])):
                user.pop('user__password')
                user.pop('user__is_active')
                token, created = Token.objects.get_or_create(user=user['user'])
                return Response({"message": "Login exitoso",  "code": 200, "token": token.key, "data":  user})
            else:
                message= "Contraseña incorrecta"
                return Response({"message": message , "code": 500, 'data': {}} )     

        else:
            message = "El id proporcionado no existe"
            return Response({"message": message , "code": 500, 'data': {}} )
    else:
        message = "El usuario no está activo o no ha proporciando datos validos"
        return Response({"message": message , "code": 500, 'data': {}})



#========== CRUD para la informacion basica del usuario ==========
#Listar todos los usuarios
class UserList(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
#    permission_classes = (AllowAn,)


#Listar un usuario por id
class UserDetail(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


#Crear un usuario
class UserCreate(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CreateUserSerializer
   

#Actualizar datos de un usuario por id
class UserUpdate(UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UpdateUserSerializer


#Eliminar usuario
class DeleteUser(DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


#========== CRUD para la informacion del cliente ==========
#Listar todos los clientes (anida info basica de usuario)
class ClientList(ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


#Listar un cliente por id
class ClientDetail(RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


#Crear cliente asignando un usuario ya existente
class ClientCreate(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = CreateClientSerializer



#Crear cliente incluyendo usuario al mismo tiempo
class NewClientCreate(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = CreateNewClientSerializer


#Actualizar datos de Cliente por id
class ClientUpdate(UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = UpdateClientSerializer


#Eliminar Un cliente sin afectar usuario
class DeleteClient(DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


#========== CRUD para la informacion del trabajador ==========
#Listar todos los trabajadores
class WorkerList(ListAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


#Listar un cliente por id
class WorkerDetail(RetrieveAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


#Crear un trabajador para asignar a usuario existente
class CreateWorker(ListCreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


#Crear cliente incluyendo usuario al mismo tiempo
class NewWorkerCreate(ListCreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = CreateNewWorkerSerializer


#Actualizar datos del trabajador por id
class WorkerUpdate(UpdateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


#Eliminar Un trabajador sin afectar usuario
class DeleteWorker(DestroyAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


"""
class ClientList(ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClientSerializers

class ClientCreate(ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = RegisterClientSerializer
"""