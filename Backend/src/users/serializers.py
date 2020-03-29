from rest_framework import serializers
from users.models import CustomUser, Client, Worker
from django.contrib.auth.hashers import make_password

#========== Serializador para el usuario ========== 
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['id', 'id_user', 'name', 'email', 'password', 'phone', 'address', 'date_of_birth', 'is_admin', 'is_active', 'is_staff', 'is_superuser']


#========== Serializador para crear el usuario ========== 
class CreateUserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=128, style={'input_type': 'password'})

    class Meta:
        model = CustomUser
        fields = ['id_user', 'name', 'email', 'password', 'phone', 'address', 'date_of_birth', 'is_admin', 'is_active', 'is_staff', 'is_admin', 'is_superuser']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = CustomUser.objects.create(
            id_user=validated_data['id_user'],
            name=validated_data['name'],
            email=validated_data['email'],
            password=make_password(validated_data['password']),
            phone = validated_data['phone'],
            address=validated_data['address'],
            date_of_birth=validated_data['date_of_birth'],
            is_active=validated_data['is_active'],
            is_admin=validated_data['is_admin'],
            is_staff=validated_data['is_staff'],
            is_superuser=validated_data['is_superuser']
        )
        user.save()
        return user  


#========== Serializador para actualizar el usuario ========== 
class UpdateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'password', 'phone', 'address', 'is_active']

    def update(self, instance, validated_data):
        print(validated_data)
        validated_data['password'] = make_password(validated_data['password'])
        user = super().update(instance, validated_data)
        return user

           
#========== Serializador para el cliente ========== 
class ClientSerializer(serializers.ModelSerializer):
    
    user = UserSerializer()
    class Meta:
        model = Client
        fields = [
            'id',            
            'type_client', 
            'interes_mora', 
            'category', 
            'cycle', 
            'contrat_number',
            'estrato',
            'billing',
            'financial_state',
            'user', 
        ]

#========== Serializador para crear el cliente ========== 
class CreateClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = [
            'user', 
            'type_client', 
            'interes_mora', 
            'category', 
            'cycle', 
            'contrat_number',
            'estrato',
            'billing',
            'financial_state'
        ]


#========== Serializador para crear cliente con usuario ========== 
class CreateNewClientSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    class Meta:
        model = Client
        fields = [            
            'type_client', 
            'interes_mora', 
            'category', 
            'cycle', 
            'contrat_number',
            'estrato',
            'billing',
            'financial_state',
            'user', 
        ]

    def create(self, validated_data):
        usuario = validated_data.pop('user')
        usuario['password'] = make_password(usuario['password'])
        custom = CustomUser.objects.create(**usuario)
        #cliente['user'] = custom
        """
        cliente = Client.objects.create(
            user=custom,
            type_client=validated_data['type_client'],
            interes_mora=validated_data['interes_mora'],
            category=validated_data['category'],
            cycle=validated_data['cycle'],
            contrat_number=validated_data['contrat_number'],
            estrato=validated_data['estrato'],
            billing=validated_data['billing'],
            financial_state=validated_data['financial_state'],
        )
        cliente.save()
        """
        cliente = Client.objects.create(user=custom, **validated_data)
        return cliente        

#========== Serializador para actualizar el cliente ========== 
class UpdateClientSerializer(serializers.ModelSerializer):

    #usuario = UserSerializer()
    class Meta:
        model = Client
        fields = [
            'type_client', 
            'interes_mora',
            'category',
            'cycle',
            'contrat_number',
            'estrato',
            'billing',
            'financial_state'
        ]

    def update(self, instance, validated_data):
        print("===============IMPORMIENDO================")
        print(validated_data)
        #validated_data['password'] = make_password(validated_data['password'])
        user = super().update(instance, validated_data)
        return user

#========== Serializador para el trabajador ========== 
class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = [
            'id', 'user', 'user_type'
        ]

#========== Serializador: crea trabajador con usuario al tiempo ========== 
class CreateNewWorkerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Worker
        fields = ['id', 'user_type', 'user']

    def create(self, validated_data):
        usuario = validated_data.pop('user')
        usuario['password'] = make_password(usuario['password'])
        custom = CustomUser.objects.create(**usuario)
        worker = Worker.objects.create(user=custom, **validated_data)
        return worker  
"""
class ClientSerializers(serializers.ModelSerializer):
    
    usuario = UserSerializer(read_only=True)
    #userId = serializers.PrimaryKeyRelatedField(write_only=True, queryset=CustomUser.objects.all(), source='usuario')

    class Meta:
        model = Cliente
        fields = ['biography', 'usuario']


class RegisterClientSerializer(serializers.ModelSerializer):

    #usuario = UserSerializer(many=False, read_only=True)

    usuario = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    
    class Meta:
        model = Cliente
        fields = ['biography', 'usuario']

    def create(self, validated_data):
        user = User.objects.create_user()
        return user


class RegisterClientSerializer(serializers.ModelSerializer):
    usuario = UserSerializer()

    #usuario_cliente = UserSerializer(many=False, read_only=True)
    #id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=CustomUser.objects.all(), source='usuario_cliente')

    #usuario_cliente = serializers.PrimaryKeyRelatedField(many=False, queryset=CustomUser.objects.all(), write_only=True)
    class Meta:
        model = Cliente
        fields = ['biography', 'usuario']

    def create(self, validated_data):
        client_user = validated_data.pop('usuario')
        cliente = Cliente.objects.create(**validated_data)
        print("El cliente" + client_user)
        CustomUser.objects.create(cliente=cliente, **client_user)
        return cliente

"""