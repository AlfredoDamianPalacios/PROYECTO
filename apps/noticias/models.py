from django.db import models

class Categoria(models.Model):
	nombre = models.CharField(max_length = 60)
	
	def __str__(self):
		return self.nombre

class Noticia(models.Model):
	titulo = models.CharField(max_length= 150)
	cuerpo = models.TextField(max_length = None)
	imagen = models.ImageField(upload_to = 'noticias')
	fecha = models.DateTimeField(auto_now_add=True)
	categoria_noticias = models.ForeignKey(Categoria, on_delete = models.CASCADE)

	def __str__(self):
		return self.titulo