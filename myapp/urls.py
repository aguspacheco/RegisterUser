from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from page import views 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('index/', views.index, name='index'),
    path('vertramite/', views.vertramite, name='vertramite'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('update-user/', views.update_user, name='update_user'),
    path('signup/', views.signup, name="signup"),
    path('logout/', views.salir, name="logout"),
    path('signin/', views.signin, name="signin"),
    path('datos/', views.datos, name='datos'),
    path('formulario/', views.ejidos_view, name='formulario'),
    path('salir/', views.salir, name='salir'),
    path('login/', LoginView.as_view(template_name='principal.html'), name='login'),  
    path('crear-formulario/', views.crear_formulario, name='crear_formulario'),
    path('formulario-exito/', views.formulario_exito, name="formulario_exito"),

    # Recuperacion de contraseña  
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html', email_template_name='password_reset_email.html'), name='password_reset'), 
]
