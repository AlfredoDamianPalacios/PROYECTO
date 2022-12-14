from django.urls import path
from . import views

app_name = 'noticias'
urlpatterns = [
    path('', views.Listar_Noticias, name = 'listar'),
    path('detalle/<int:pk>', views.Detalle_Noticias, name = 'detalle'),
    path('Comentario/', views.Comentar_Noticia, name = 'comentar'),
    path('borrar/<int:id>', views.Borrar_Com, name = 'borrar'),
    ]