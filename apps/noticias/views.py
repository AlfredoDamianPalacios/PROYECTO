from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Noticia
# Create your views here.

@login_required
def Listar_Noticias(request):
	contexto = {}

	#devuelve todos los objetos
	n = Noticia.objects.all() #DEVUELVE UNA LISTA DE LAS NOTICIAS
	
	contexto["noticias"] = n
	return render(request, 'Noticias/listar.html', contexto)

@login_required
def Detalle_Noticias(request, pk):
	contexto = {}
	n = Noticia.objects.get(pk = pk) # DEVUELVE LA NOTICIA REFERIDA AL PK QUE SE LE PASO
	contexto["noticia"] = n
	return render(request, 'Noticias/detalle.html',contexto)

	"""
	#devuelve un solo objeto
	x = Noticia.objects.get(pk = 1)
	print(f"Noticia 1: {x}")
	#Devuelve una categoria
	f = Noticia.objects.filter(categoria_noticias = 2)
	print(f"SOLO DEPORTES: {f}")
	"""


   
