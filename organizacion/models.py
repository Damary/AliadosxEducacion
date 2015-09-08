# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import Permission, User, Group


# Create your models here.

class Sector (models.Model):
	nombre = models.CharField (max_length = 50, help_text = u'Ingrese el sector (Gobierno, Privada, ONG) de la Organizacion')
	descripcion = models.CharField (max_length = 100)

	def __unicode__ (self):
		return u'%s' %(self.nombre)

class Rubro (models.Model):
	nombre = models.CharField (max_length = 50, help_text = u'Ingrese el Rubro de la Organizacion')
	descripcion = models.CharField (max_length = 100)

	def __unicode__ (self):
		return u'%s' %(self.nombre)

class Organizacion (models.Model):
	rtn = models.CharField(max_length = 200, unique = True, help_text = u'Ingrese el RTN de la Organizacion' )
	razon_social = models.CharField (max_length = 200, help_text = u'Ingrese la Razoo Social de la Organizacion')
	nombre_comercial = models.CharField (max_length = 200, help_text = u'Ingrese el Nombre Comercial de la Organizacion')
	sector= models.ForeignKey(Sector)
	rubro= models.ForeignKey(Rubro)
	telefono = models.CharField (max_length = 15)
	correo_electronico = models.EmailField (max_length = 50)


	def __unicode__(self):
		return u'%s %s %s %s' %(self.rtn, self.nombre_comercial, self.sector, self.rubro)


class Departamento (models.Model):
	codigo = models.CharField(max_length=2, unique=True, help_text = u'Codigo Oficial del Departamento')
	nombre = models.CharField(max_length = 128, unique=True, help_text='Nombre del Departamento')

	def __unicode__ (self):
		return u'%s' %(self.nombre)

	 #para el admin, es el nombre que sera mostrado en el admin
	class Meta:
		verbose_name = 'Departamento'
		verbose_name_plural = 'Departamentos'


class Municipio (models.Model):
	codigo = models.CharField(max_length = 2, help_text=u'Codigo Oficial del municipio en el departamento')
	nombre = models.CharField(max_length = 128, help_text='Nombre del Municipio')
	departamento = models.ForeignKey (Departamento, help_text='Departamento en el cual se encuentra ubicado')

	
	def natural_key(self):
		return u'%s | %s' % (self.codigo,self.nombre)
		
	def __unicode__(self):
		if (len(str(self.codigo)) < 2):
			codigo = '0' + str(self.codigo)
		else:
			codigo = str(self.codigo)

		return u'' + codigo + ' | ' + self.nombre

	class Meta:
		verbose_name = 'Municipio'
		verbose_name_plural = 'Municipios'
		unique_together = (("codigo", "departamento"),)


class Aldea (models.Model):
	codigo = models.CharField (max_length = 3, help_text=u'Codigo Oficial de la aldea')
	nombre = models.CharField (max_length = 128, help_text= u'Nombre de la Aldea')
	municipio= models.ForeignKey (Municipio, help_text=u'Municipio donde se encuentra ubicada la aldea')

	def natural_key(self):
		return u'%s | %s' % (self.codigo, self.nombre)

	def __unicode__(self):
		if (len(str(self.codigo)) < 2):
			codigo = '00' + str(self.codigo)
		else:
			if (len(str(self.codigo)) < 3):
				codigo = '0' + str(self.codigo)
			else:
				codigo = str(self.codigo)

		return u'%s | %s ' % (codigo,self.nombre)

	class Meta:
		verbose_name = 'Aldea'
		verbose_name_plural = 'Aldeas'

class Sucursal (models.Model):
	organizacion= models.ForeignKey (Organizacion)
	departamento = models.ForeignKey(Departamento)
	municipio = models.ForeignKey(Municipio)
	aldea = models.ForeignKey(Aldea)
	direccion_completa = models.CharField(max_length = 100)
	descripcion = models.TextField(max_length = 300)

	def __unicode__ (self):
		return u'%s %s %s' %(self.organizacion, self.departamento, self.municipio)


class Categoria (models.Model):
	nombre_categoria = models.CharField (max_length = 75)
	descripcion = models.CharField (max_length = 200)

	def __unicode__ (self):
		return u'%s %s' %( self.nombre_categoria, self.descripcion)


class SubCategoria(models.Model):
	area = models.ForeignKey(Categoria)
	nombre = models.CharField (max_length = 100)
	descripcion = models.CharField (max_length = 200)

	def __unicode__ (self):
		return u'%s, %s' % (self.area, self.nombre_sub_categoria)


class PresupuestoDonacion (models.Model):
	organizacion = models.ForeignKey (Organizacion)
	fecha_inicio = models.DateField 
	fecha_final = models.DateField
	categoria = models.ForeignKey(Categoria)
	monto_total = models.PositiveSmallIntegerField (help_text = 'Monto Total de la Donacion')
	usuario_creador = models.ForeignKey(User, related_name='r_inasistencia_creador', null=True, blank=True)
	usuario_modifico = models.ForeignKey(User, related_name='r_inasistencia_modificador', null=True, blank=True)
	fecha_creacion = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	fecha_modificacion = models.DateTimeField(auto_now=True, null=True, blank=True) 

	def __unicode__ (self):
		return u'%s %s %s'(self.organizacion, self.categoria, self.monto_total)









