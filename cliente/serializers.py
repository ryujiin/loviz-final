from models import *
from rest_framework import serializers
from django.contrib.auth.models import User as User
from cliente.models import Cliente


class DireccionSerilizer(serializers.ModelSerializer):
	class Meta:
		model = Direccion
		fields = ('__all__')

class ClienteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cliente
		fields = ('__all__')


class UsuarioSerializer(serializers.ModelSerializer):
	cliente = ClienteSerializer()
	direcciones = DireccionSerilizer(many=True, read_only=True)

	class Meta:
		model = User
		fields = ('id','username','first_name','last_name','email','cliente','direcciones')

class PerfilUSerSerializer(serializers.ModelSerializer):
	email = serializers.SerializerMethodField('get_email')
	nombre = serializers.SerializerMethodField('get_nombre')
	apellido = serializers.SerializerMethodField('get_apellido')
	class Meta:
		model = Cliente
		fields = ('id','usuario','nombre','apellido','email','dni','telefono','direcciones')

	def get_email(self,obj):
		return obj.usuario.email

	def get_nombre(self,obj):
		return obj.usuario.first_name

	def get_apellido(self,obj):
		return obj.usuario.last_name



class UserSerializer(serializers.ModelSerializer):
	foto = serializers.SerializerMethodField()
	direcciones = DireccionSerilizer()

	class Meta:
		model=User
		fields = ('username','password', 'first_name', 'last_name', 'email','is_staff','foto','direcciones')
		write_only_fields = ('password',)

	def restore_object(self, attrs, instance=None):
		user = super(UserSerializer, self).restore_object(attrs, instance)
		user.set_password(attrs['password'])
		return user

	def get_foto(self,obj):
		foto ='enrique'
		return foto

class SuscritoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Suscrito
		fields = ('__all__')

class MayoristaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Mayorista