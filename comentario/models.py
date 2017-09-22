from __future__ import unicode_literals

from django.db import models
from catalogo.models import Producto
from django.contrib.auth.models import User as User


# Create your models here.
class Comentario(models.Model):
	producto = models.ForeignKey(Producto,blank=True,null=True)
	usuario = models.ForeignKey(User, null=True,blank=True)
	verificado = models.BooleanField(default=False)
	valoracion = models.PositiveIntegerField(default=0)
	comentario = models.TextField(blank=True)
	email_invitado = models.CharField(max_length=100,blank=True,null=True)
	creado = models.DateTimeField(auto_now_add=True)
	full_name_invitado = models.CharField(max_length=100,blank=True)
	apellido_invitado = models.CharField(max_length=100,blank=True)

class ComentarioImagen(models.Model):
	comentario = models.ForeignKey(Comentario,blank=True,null=True,related_name='fotos_comentario')
	foto = models.ImageField(upload_to='comentarios',blank=True,null=True,max_length=250)    