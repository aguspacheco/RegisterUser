from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from page import views 

urlpatterns = [
    #Pagina principal e inicio de seccion
    path('', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.salir, name='logout'),
    path('signin/', views.signin, name="signin"),
    path('index/', views.index, name='index'),

    #Vistas estaticas 
    path('password_reset_complete/', views.password_reset_complete, name='password_reset_complete'),
    path('vertramite/', views.vertramite, name='vertramite'),
    path('formulario/', views.ejidos_view, name='formulario'),
    path('formulario-exito/', views.formulario_exito, name="formulario_exito"),

    #Vistas para formularios y datos del usuario
    path('datos_usuario/', views.datos_usuario, name='datos_usuario'),
    path('update-user/', views.update_user, name='update_user'),
    path('ejidos/', views.ejidos_view, name='ejidos'),
    path('crear-formulario/', views.CrearFormulario.as_view(), name='crear_formulario'),

    
    #Administracion
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]