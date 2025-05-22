"""
URL configuration for Vinyles project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from asistencia import views


urlpatterns = [
    # USUARIO NORMAL
    path('admin/', admin.site.urls, name='admin'),
    path('', views.inicio, name='inicio'),
    path('albumes/', views.albumes, name='albumes'),
    path('codigoRecuperacion/', views.codigoRecuperacion, name='codigoRecuperacion'),
    path('ddl/', views.ddl, name='ddl'),
    path('login/', views.login, name='login'),
    path('loginAdministrador/', views.loginAdministrador, name='loginAdministrador'),
    path('registro/', views.registro, name='registro'),
    path('restablecerContrasena/', views.restablecerContrasena, name="restablecerContrasena"),
    path('restablecerContrasenaAdmin/', views.restablecerContrasenaAdmin, name='restablecerContrasenaAdmin'),
    path('sobreNosotros/', views.sobreNosotros, name='sobreNosotros'),
    path('sobreNosotrosAdmin/', views.sobreNosotrosAdmin, name='sobreNosotrosAdmin'),
    path('sobreNosotrosCom/', views.sobreNosotrosCom, name='sobreNosotrosCom'),
    path('sobreNosotrosVen/', views.sobreNosotrosVen, name='sobreNosotrosVen'),
    path('terCon/', views.terCon, name='terCon'),
    path('vinilo/', views.vinilo, name='vinilo'),


    # USUARIO COMPRADOR
    path('albumesCom/', views.albumesCom, name='albumesCom'),
    path('carrito/', views.carrito, name='carrito'),
    path('checkout/', views.checkout, name='checkout'),
    path('inicioCom/', views.inicioCom, name='inicioCom'),
    path('perfil/', views.perfil, name='perfil'),
    path('progresoEnvio/', views.progresoEnvio, name='progresoEnvio'),
    path('reembolsos/', views.reembolsos, name='reembolsos'),
    path('soporte/', views.soporte, name='soporte'),

    # USUARIO VENDEDOR
    path('AlbumBadVendedor/', views.albumBadVendedor, name='albumBadVendedor'),
    path('crear/', views.crear, name='crear'),
    path('notificacionesVen/', views.notificacionesVen, name='notificacionesVen'),
    path('perfilVen/', views.perfilVen, name='perfilVen'),
    path('producto/', views.producto, name='producto'),
    
    # ADMINISTRADOR
    path('administrador/', views.administrador, name = 'administrador'),
    path('adminNotificaciones', views.adminNotificaciones, name='adminNotificaciones'),
    path('adminPedido/', views.adminPedido, name = 'adminPedido'),
    path('adminProducto/', views.adminProducto, name = 'adminProducto'),
    path('adminReembolsos', views.adminReembolsos, name='adminReembolsos'),
    path('adminUsuario/', views.adminUsuario, name = 'adminUsuario'),
    path('adminVerificacion/', views.adminVerificacion, name = 'adminVerificacion'),
    path('adPro/', views.adPro, name = 'adPro'),
    path('bloqUsers', views.bloqUsers, name='bloqUsers'),
    path('generos/', views.generos, name='generos'),
    path('gestionUsers', views.gestionUsers, name='gestionUsers'),
    path('logOut/', views.logOut, name='logOut'),
    path('newUsers', views.newUsers, name='newUsers'),
    path('pedidoPendiente', views.pedidoPendiente, name='pedidoPendiente'),
    path('pedidoRealizado', views.pedidoRealizado, name='pedidoRealizado'),
    path('ventas/', views.ventas, name='ventas'),
    path('masvendidos/', views.masVendidos, name='masVendidos'),

    # ALBUMES
    path('bts/', views.bts, name='bts'),
    path('cartiMusic/', views.cartiMusic, name='cartiMusic'),
    path('eminemShow', views.eminemShow, name='eminemShow'),
    path('exitosJoe/', views.exitosJoe, name='exitosJoe'),
    path('gnrAppetite/', views.gnrAppetite, name='gnrAppetite'),
    path('master/', views.master, name='master'),
    path('mjBad', views.mjBad, name='mjBad'),
    path('mjThriller/', views.mjThriller, name='mjThriller'),
    path('nirvana/', views.nirvana, name='nirvana'),
    path('theBeatles/', views.theBeatles, name='theBeatles'),

    #USUARIOS
    path('lauraG/', views.lauraG, name='lauraG'),
    path('carlosR/', views.carlosR, name='carlosR'),
    path('camilaQ/', views.camilaQ, name='camilaQ'),
    path('jhonM/', views.jhonM, name='jhonM'),
    path('alexR/', views.alexR, name='alexR'),
    path('andreaVillalobos', views.andreaVillalobos, name='andreaVillalobos'),
    path('benjaminCastro', views.benjaminCastro, name='benjaminCastro'),
    path('crisitanDominguez', views.cristianDominguez, name='cristianDominguez'),
    path('angelaTorres', views.angelaTorres, name='angelaTorres'),
    path('elisaNaranjo', views.elisaNaranjo, name='elisaNaranjo'),
    path('emilioTorres', views.emilioTorres, name='emilioTorres'),
    path('andreaVillalobos2', views.andreaVillalobos2, name='andreaVillalobos2'),
    path('benjaminCastro2', views.benjaminCastro2, name='benjaminCastro2'),
    path('crisitanDominguez2', views.cristianDominguez2, name='cristianDominguez2'),
    path('angelaTorres2', views.angelaTorres2, name='angelaTorres2'),
    path('elisaNaranjo2', views.elisaNaranjo2, name='elisaNaranjo2'),
    path('emilioTorres2', views.emilioTorres2, name='emilioTorres2'),
    path('sofiaRamirez', views.sofiaRamirez, name='sofiaRamirez'),
    path('esperanzaBarrera', views.esperanzaBarrera, name='esperanzaBarrera'),
    path('fernandoMolina', views.fernandoMolina, name='fernandoMolina'),
]