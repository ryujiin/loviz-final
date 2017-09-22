from models import *
from rest_framework import serializers
from django.contrib.auth.models import User as User

class ComentarioImagenSerializer(serializers.ModelSerializer):
	class Meta:
		model = ComentarioImagen
		fields = ('__all__')

from django.utils.timesince import timesince

class ComentairoSerializer(serializers.ModelSerializer):
	creado = serializers.SerializerMethodField('get_tiempo_creado')
	nombre = serializers.SerializerMethodField('get_nombre_user')
	img_producto = serializers.SerializerMethodField('get_img')
	fotos_comentario = ComentarioImagenSerializer(many=True,read_only=True)
	class Meta:
		model = Comentario
		fields = ('id','verificado',
			'email_invitado',
			'valoracion',
			'comentario',
			'creado',
			'producto',
			'usuario',
			'nombre',
			'img_producto',
			'fotos_comentario',
			'full_name_invitado',
			'apellido_invitado')

	def get_tiempo_creado(self,obj):
		time = timesince(obj.creado)
		return time

	def get_nombre_user(self,obj):
		nombre = ''
		if obj.usuario:
			nombre = obj.usuario.username 
			if obj.usuario.first_name:
				nombre = "%s %s" %(obj.usuario.first_name,obj.usuario.last_name)
		else:
			nombre = "%s %s" %(obj.full_name_invitado,obj.apellido_invitado) 
		return nombre

	def get_img(self,obj):
		return obj.producto.get_thum()
