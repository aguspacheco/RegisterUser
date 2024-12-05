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
    path('reset-password/', views.password_reset_request, name="password_reset_request"),  
    path("reset-password/confirmation/", views.password_reset_confirmation, name="password_reset_confirmation"),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('tramiteUser/', views.tramiteUser, name='tramiteUser'),
    path('formulario/', views.ejidos_view, name='formulario'),
    path('formulario-exito/', views.formulario_exito, name="formulario_exito"),

    #Vistas para formularios y datos del usuario
    path('datos_usuario/', views.datos_usuario, name='datos_usuario'),
    path('update-user/', views.update_user, name='update_user'),
    path('ejidos/', views.ejidos_view, name='ejidos'),
    path('crear-formulario/', views.CrearFormulario.as_view(), name='crear_formulario'),
    path('date_form/', views.date_form, name='date_form'),
    
    #Administracion
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]   