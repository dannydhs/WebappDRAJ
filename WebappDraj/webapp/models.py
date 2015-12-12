# -*- encoding: utf-8 -*-
from django.db import models
from decimal import Decimal
from datetime import datetime 

class Sector(models.Model):
	nombre = models.CharField(max_length=30)

	def __unicode__(self):              
		return self.nombre

class Subsector(models.Model):
	nombre = models.CharField(max_length=30)
	sector = models.ForeignKey(Sector, null=True, blank=True)

	def __unicode__(self):              
		return self.nombre

class Producto(models.Model):
	nombre = models.CharField(max_length=30, null=True, blank=True)
	subsector = models.ForeignKey(Subsector, null=True, blank=True)

	def __unicode__(self):              
		return self.nombre

class Produccion(models.Model):
	valor_bruto_pinicial = models.DecimalField(max_digits=8, decimal_places=5)
	periodo_inicial_anio = models.CharField(max_length=4, null=True, blank=True)
	periodo_inicial_mes = models.CharField(max_length=2, null=True, blank=True)
	valorbruto_pfinal = models.DecimalField(max_digits=8, decimal_places=5)
	periodo_final_anio = models.CharField(max_length=4, null=True, blank=True)
	periodo_final_mes = models.CharField(max_length=2, null=True, blank=True)
	variacion = models.DecimalField(max_digits=8, decimal_places=5)
	indice_cantidad = models.DecimalField(max_digits=8, decimal_places=5)
	producto = models.ForeignKey(Producto, null=True, blank=True)

	def __unicode__(self): 
		return unicode(self.variacion)

"""
class Producto(models.Model):
	nombre = models.CharField(max_length=30, null=True, blank=True)

	def __unicode__(self):              
		return self.nombre

class Produccion_periodo_inicial(models.Model):
	valor = models.DecimalField(max_digits=8, decimal_places=5)
	anio = models.CharField(max_length=4, null=True, blank=True)
	mes = models.CharField(max_length=2, null=True, blank=True)
	producto = models.ForeignKey(Producto, null=True, blank=True)

	def __unicode__(self): 
		return unicode(self.valor)

class Produccion_periodo_final(models.Model):
	valor = models.DecimalField(max_digits=8, decimal_places=5)
	anio = models.CharField(max_length=4, null=True, blank=True)
	mes = models.CharField(max_length=2, null=True, blank=True)
	producto = models.ForeignKey(Producto, null=True, blank=True)

	def __unicode__(self): 
		return unicode(self.valor)

class Produccion_resultado(models.Model):
	produccion_periodo_inicial = models.ForeignKey(Produccion_periodo_inicial, null=True, blank=True)
	produccion_periodo_final = models.ForeignKey(Produccion_periodo_final, null=True, blank=True)
	variacion = models.DecimalField(max_digits=8, decimal_places=5)
	indice_cantidad = models.DecimalField(max_digits=8, decimal_places=5)

	def __unicode__(self):
		return unicode(self.variacion)
"""


"""
class Periodo_inicial(models.Model):
	fecha = models.DateField()
	valor_bruto = models.DecimalField(max_digits=5, decimal_places=3)

class Periodo_final(models.Model):
	fecha = models.DateField()
	valor_bruto = models.DecimalField(max_digits=5, decimal_places=3)

class Sub_sector(models.Model):
	idsubsector = models.AutoField(primary_key=True)
	nombre = models.CharField(max_length=30)
	descripcion = models.CharField(max_length=100)
	variacion = models.DecimalField(max_digits=5, decimal_places=2)
	ind_cant = models.DecimalField(max_digits=5, decimal_places=2)
	pinicial = models.ForeignKey(Periodo_inicial)
	pfinal = models.ForeignKey(Periodo_final)
	producto = models.ForeignKey(Productos, null=True, blank=True)
	
	def __unicode__(self):              
		return self.nombre

class Sector(models.Model):
	nombre = models.CharField(max_length=30)
	descripcion = models.CharField(max_length=100)
	sbsector = models.ForeignKey(Sub_sector)
	
	def __unicode__(self):              
		return self.nombre
"""

