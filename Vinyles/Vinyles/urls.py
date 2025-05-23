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
    path('', views.pub_inicio, name='pub_inicio'),
    path('pub_albumes/', views.pub_albumes, name='pub_albumes'),
    path('pub_codigo_recuperacion/', views.pub_codigo_recuperacion, name='pub_codigo_recuperacion'),
    path('pub_ddl/', views.pub_ddl, name='pub_ddl'),
    path('pub_login/', views.pub_login, name='pub_login'),
    path('pub_login_administrador/', views.pub_login_administrador, name='pub_login_administrador'),
    path('pub_registro/', views.pub_registro, name='pub_registro'),
    path('pub_restablecer_contrasena/', views.pub_restablecer_contrasena, name="pub_restablecer_contrasena"),
    path('pub_restablecer_contrasena_admin/', views.pub_restablecer_contrasena_admin, name='pub_restablecer_contrasena_admin'),
    path('pub_sobre_nosotros/', views.pub_sobre_nosotros, name='pub_sobre_nosotros'),
    path('pub_ter_con/', views.pub_ter_con, name='pub_ter_con'),
    path('pub_vinilo/', views.pub_vinilo, name='vinilo'),
    path('pub_logOut/', views.pub_logOut, name='pub_logOut'),


    # USUARIO COMPRADOR
    path('com_albumes/', views.com_albumes, name='com_albumes'),
    path('com_carrito/', views.com_carrito, name='com_carrito'),
    path('com_checkout/', views.com_checkout, name='com_checkout'),
    path('com_inicio/', views.com_inicio, name='com_inicio'),
    path('com_perfil/', views.com_perfil, name='com_perfil'),
    path('com_progreso_envio/', views.com_progreso_envio, name='com_progreso_envio'),
    path('reembolsos/', views.reembolsos, name='reembolsos'),
    path('soporte/', views.soporte, name='soporte'),
    path('com_sobre_nosotros/', views.com_sobre_nosotros, name='com_sobre_nosotros'),
    


    # USUARIO VENDEDOR
    path('ven_bad/', views.ven_bad, name='ven_bad'),
    path('ven_crear/', views.ven_crear, name='ven_crear'),
    path('ven_notificaciones/', views.ven_notificaciones, name='ven_notificaciones'),
    path('ven_perfil/', views.ven_perfil, name='ven_perfil'),
    path('ven_producto/', views.ven_producto, name='ven_producto'),
    path('ven_sobre_nosotros/', views.ven_sobre_nosotros, name='ven_sobre_nosotros'),
    
    # ADMINISTRADOR
<<<<<<< HEAD
    path('admin_administrador/', views.admin_administrador, name = 'admin_administrador'),
    path('admin_notificaciones/', views.admin_notificaciones, name='admin_notificaciones'),
    path('admin_pedido/', views.admin_pedido, name = 'admin_pedido'),
    path('admin_producto/', views.admin_producto, name = 'admin_producto'),
    path('admin_reembolsos', views.admin_reembolsos, name='admin_reembolsos'),
    path('admin_usuario/', views.admin_usuario, name = 'admin_usuario'),
    path('admin_verificacion/', views.admin_verificacion, name = 'admin_verificacion'),
    path('admin_adPro/', views.admin_adPro, name = 'admin_adPro'),
    path('admin_bloq_users', views.admin_bloq_users, name='admin_bloq_users'),
    path('admin_generos/', views.admin_generos, name='admin_generos'),
    path('admin_gestion_users/', views.admin_gestion_users, name='admin_gestion_users'),
    path('admin_new_users', views.admin_new_users, name='admin_new_users'),
    path('admin_pedido_pendiente', views.admin_pedido_pendiente, name='admin_pedido_pendiente'),
    path('admin_pedido_realizado', views.admin_pedido_realizado, name='admin_pedido_realizado'),
    path('admin_ventas/', views.admin_ventas, name='admin_ventas'),
    path('admin_sobre_nosotros/', views.admin_sobre_nosotros, name='admin_sobre_nosotros'),
=======
    path('administrador/', views.administrador, name = 'administrador'),
    path('notificaciones/', views.notificaciones, name='notificaciones'),
    path('pedido/', views.pedido, name = 'pedido'),
    path('producto/', views.producto, name = 'producto'),
    path('reembolsos', views.reembolsos, name='reembolsos'),
    path('usuario/', views.usuario, name = 'usuario'),
    path('verificacion/', views.verificacion, name = 'verificacion'),
    path('adPro/', views.adPro, name = 'adPro'),
    path('bloq_users', views.bloq_users, name='bloq_users'),
    path('generos/', views.generos, name='generos'),
    path('gestion_users/', views.gestion_users, name='gestion_users'),
    path('logOut/', views.logOut, name='logOut'),
    path('new_users', views.new_users, name='new_users'),
    path('pedido_pendiente', views.pedido_pendiente, name='pedido_pendiente'),
    path('pedido_realizado', views.pedido_realizado, name='pedido_realizado'),
    path('ventas/', views.ventas, name='ventas'),
    path('masvendidos/', views.masVendidos, name='masVendidos'),
>>>>>>> 416749546cd19afe9220b010069789be648bd8bb

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