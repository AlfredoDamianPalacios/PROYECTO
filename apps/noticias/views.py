from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Noticia, Categoria, Comentario
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy, reverse

# Create your views here.

@login_required
def Listar_Noticias(request):
	contexto = {}

	id_categoria = request.GET.get("id", None)

	if id_categoria:
		n = Noticia.objects.filter(categoria_noticias = id_categoria)
	else:
		n = Noticia.objects.all() #DEVUELVE UNA LISTA DE LAS OBJETOS
	
	contexto["noticias"] = n

	cat = Categoria.objects.all().order_by('nombre')
	contexto['categorias'] = cat
	return render(request, 'Noticias/listar.html', contexto)

@login_required
def Detalle_Noticias(request, pk):
	contexto = {}

	n = Noticia.objects.get(pk = pk) # DEVUELVE LA NOTICIA REFERIDA AL PK QUE SE LE PASO
	contexto["noticia"] = n

	c = Comentario.objects.filter(noticia = n)
	contexto['comentarios'] = c

	return render(request, 'Noticias/detalle.html',contexto)

	"""
	#devuelve un solo objeto
	x = Noticia.objects.get(pk = 1)
	print(f"Noticia 1: {x}")
	#Devuelve una categoria
	f = Noticia.objects.filter(categoria_noticias = 2)
	print(f"SOLO DEPORTES: {f}")
	"""
@login_required
def Comentar_Noticia(request):
	com = request.POST.get('comentario',None)
	usu = request.user
	noti = request.POST.get('id_noticia', None)# OBTENGO LA PK
	noticia = Noticia.objects.get(pk = noti) #BUSCO LA NOTICIA CON ESA PK
	coment = Comentario.objects.create(usuario = usu, noticia = noticia, texto = com)

	return redirect(reverse_lazy('noticias:detalle', kwargs={'pk': noti}))

#Borrar comentario, espero ...
@login_required
def Borrar_Com(request, id):
	id_noti= None
	try:
		coment= Comentario.objects.get(pk = id)
		id_noti= coment.noticia.pk
		coment.delete()
	except Exception as a:
		print("Comentario no existe")
	return redirect(reverse_lazy('noticias:detalle', kwargs={'pk': id_noti}))












#{'nombre':'nicolas', 'apellido':'Tortosa', 'edad':33}
#EN EL TEMPLATE SE RECIBE UNA VARIABLE SEPARADA POR CADA CLAVE VALOR
# nombre
# apellido
# edad

'''
ORM
CLASE.objects.get(pk = ____)
CLASE.objects.filter(campos = ____)
CLASE.objects.all() ---> SELECT * FROM CLASE
'''