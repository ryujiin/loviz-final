from django.db import models
from django.template.defaultfilters import slugify

from sorl.thumbnail import get_thumbnail
from django.contrib.auth.models import User as User
from utiles.models import Color,Talla
from material.models import Material,PrecioMaterial

from datetime import datetime, timedelta, time
from django.utils import timezone

from django.conf import settings


# Create your models here.
class Producto(models.Model):
	nombre = models.CharField(max_length=120,blank=True,null=True)
	full_name = models.CharField(max_length=120, unique=True,blank=True,null=True,editable=False)
	slug = models.CharField(max_length=120,editable=False,unique=True)
	color = models.ForeignKey(Color,blank=True,null=True)
	relaciones = models.ManyToManyField('self',blank=True, related_name='colores')
	categorias = models.ManyToManyField('Categoria',blank=True,related_name='categorias_producto')
	activo = models.BooleanField(default=True)
	descripcion = models.TextField(blank=True,null=True)
	creado = models.DateTimeField(auto_now_add=True)
	actualizado = models.DateTimeField(auto_now=True)
	modelo = models.ForeignKey('Modelo',blank=True,null=True)
	video = models.CharField(max_length=120, blank=True,null=True)
	vendidos = models.PositiveIntegerField(default=0,editable=False)
	en_oferta = models.BooleanField(default=False)

	def __unicode__(self):
		return self.full_name

	def save(self, *args, **kwargs):
		self.full_name = "%s (%s)" %(self.nombre,self.color)
		if not self.slug:
			self.slug = slugify(self.full_name)
		super(Producto, self).save(*args, **kwargs)

	def get_thum(self):
		img = ProductoImagen.objects.filter(producto=self).order_by('pk')[0]
		img = get_thumbnail(img.foto, '450x350', quality=80)
		return '%s%s'  %(settings.SITE_NAME,img.url)

	def get_thum2(self):
		img = ProductoImagen.objects.filter(producto=self, orden=1).order_by('pk')[:1].get()
		img = get_thumbnail(img.foto, '450x350', quality=80)
		return '%s%s'  %(settings.SITE_NAME,img.url)

	def guardar_oferta(self):
		oferta = self.get_en_oferta()
		if oferta>0:
			self.en_oferta = True
		else:
			self.en_oferta = False


	def guardar_novedad(self):
		dia_no_nuevo = timezone.now()-timedelta(days=20)
		if dia_no_nuevo > self.creado:
			return False
		else:
			return True

	def get_en_oferta(self):
		variaciones = self.get_variaciones()
		if variaciones:
			return variaciones[0].oferta
		else:
			return 0

	def get_variaciones(self):
		variaciones = ProductoVariacion.objects.filter(producto=self).order_by('-oferta')
		return variaciones

	def get_precio_lista(self):
		en_oferta = self.get_en_oferta()
		if en_oferta:
			variaciones=self.get_variaciones()
		else:
			variaciones = ProductoVariacion.objects.filter(producto=self).order_by('-precio_minorista')
		if variaciones:
			precio = variaciones[0].precio_minorista
		else:
			precio = 0
		if not precio:
			precio =0
		return precio

	def get_tallas_disponibles(self):
		tallas = ProductoVariacion.objects.filter(producto=self,stock__gt=0)
		return tallas

	def get_precio_oferta_lista(self):
		en_oferta = self.get_en_oferta()
		if en_oferta:
			variaciones=self.get_variaciones()
			precio_oferta = variaciones[0].precio_oferta
			return precio_oferta
		else:
			precio = self.get_precio_lista()
			return precio

	def get_parientes(self):
		parientes = self.parientes.all()
		return parientes

	def get_num_estrellas(self):
		num_entrellas = Comentario.objects.filter(producto=self)
		return num_entrellas

	def get_absolute_url(self):
		return "/producto/%s/" % self.slug

class Categoria(models.Model):
	SECCIONES = (
		('genero','Genero'),
		('categoria','Categoria'),
		('estilo','Estilo'),
	)
	nombre = models.CharField(max_length=120)
	full_name = models.CharField(max_length=255,db_index=True, editable=False)
	padre = models.ForeignKey('self',blank=True,null=True)
	seccion = models.CharField(max_length=100,choices=SECCIONES,blank=True,null=True)
	slug = models.SlugField(max_length=120,unique=True,editable=False)
	titulo_seo = models.CharField(max_length=100,blank=True,null=True)	
	descripcion = models.TextField(blank=True,null=True)
	activo = models.BooleanField(default=True)
	imagen = models.ImageField(upload_to='categorias',blank=True,null=True,max_length=250)

	def __unicode__(self):
		return self.slug

	def get_absolute_url(self):
		return "/catalogo/%s/" % self.slug

	def save(self, *args, **kwargs):
		if self.padre:
			self.full_name = "%s - %s" %(self.nombre, self.padre.full_name)
		else:
			self.full_name = self.nombre
		if not self.slug:
			self.slug = slugify(self.full_name)
		super(Categoria, self).save(*args, **kwargs)

class ProductoVariacion(models.Model):
	producto = models.ForeignKey(Producto,related_name='variaciones')
	talla = models.ForeignKey(Talla)
	precio_minorista = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
	oferta = models.PositiveIntegerField(default=0)
	precio_oferta = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
	stock = models.PositiveIntegerField(default=0)

	def __unicode__(self):
		return "%s - %s" %(self.producto,self.precio_minorista)

	def get_precio(self):
		if self.precio_oferta:
			precio = self.precio_oferta
		else:
			precio = self.precio_minorista
		return precio

	def save(self, *args, **kwargs):
		if not self.precio_oferta:
			if self.oferta>0:
				self.precio_oferta = self.precio_minorista - (self.precio_minorista*self.oferta/100)
		else:
			if not self.oferta:
				self.oferta = (self.precio_minorista-self.precio_oferta)*100/self.precio_minorista
		super(ProductoVariacion, self).save(*args, **kwargs)
		if self.oferta>0:
			self.producto.en_oferta = True
			self.producto.save()


def url_imagen_pr(self,filename):
	url = "productos/imagen/%s/%s" % (self.producto.pk, filename)
	return url

class ProductoImagen(models.Model):
	producto = models.ForeignKey(Producto,related_name="imagenes_producto")
	foto = models.ImageField(upload_to=url_imagen_pr)
	orden = models.PositiveIntegerField(default=0)
	creado = models.DateTimeField(auto_now_add=True)
	actualizado = models.DateTimeField(auto_now=True)
	class Meta:
		ordering = ["orden"]

	def save(self, *args, **kwargs):
		orden_anterior = ProductoImagen.objects.filter(producto=self.producto).order_by('-orden')
		if orden_anterior:
			self.orden=orden_anterior[0].orden+1
		else:
			self.orden=0
		super(ProductoImagen, self).save(*args, **kwargs)

	def get_thum_medium(self):
		img = get_thumbnail(self.foto, '740x600', quality=80)
		return img

	def get_thum(self):
		img = get_thumbnail(self.foto, '150x100', quality=80)
		return img

class MaterialProducto(models.Model):
	producto = models.ForeignKey(Producto,blank=True, related_name='material_producto')
	material = models.ForeignKey(Material,blank=True)
	vista = models.BooleanField(default=True)
	descripcion = models.CharField(max_length=300,blank=True)

	def save(self, *args, **kwargs):
		super(MaterialProducto, self).save(*args, **kwargs)


class SeccionProducto(models.Model):
	UNIDADES=(('cm','centimetro'),('und','unidad'),('m','metro'),('lt','litro'))
	nombre = models.CharField(max_length=100,blank=True)
	talla = models.ForeignKey(Talla,blank=True,null=True)
	cantidad = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,help_text='La cantidad usada en este producto de este material')
	unidad = models.CharField(max_length=10,blank=True,null=True,choices=UNIDADES)
	modelo = models.ForeignKey('Modelo',blank=True)

	def __unicode__(self):
		return self.nombre

	def save(self, *args, **kwargs):
		if not self.slug:
			slug = '%s %s' (self.nombre,self.talla.nombre)
			self.slug = slugify(slug)
		super(SeccionProducto, self).save(*args, **kwargs)


class Modelo(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.TextField(blank=True)

	def __unicode__(self):
		return self.nombre