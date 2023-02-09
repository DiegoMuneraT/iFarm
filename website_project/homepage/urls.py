from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    #path to home
    path('home/', views.home, name='home'),
    #path login
    path('', LoginView.as_view(template_name='homepage/login.html'), name='login'),
    #path to signup
    path('signForm/', views.signForm),
    #path to register user
    path('signup/', views.signup, name='signup'),
    #path to registrarCultivo function at views
    path('registrarCultivo/', views.registrarCultivo),
    #path to modificarCultivo function at views
    path('modificarCultivo/<nombre>', views.modificarCultivo),
    #path to modify function at views
    path('modificacion/', views.modificacion),
    #path to activarRiego function at views
    path('activarRiego/', views.activarRiego), #activarRiego/<nombre>
    #path to desactivarRiego function at views
    path('desactivarRiego/', views.desactivarRiego), #desactivarRiego/<nombre>
    #path to infoCultivo function at views
    path('infoCultivo/', views.infoCultivo),
    #path to CultivoEliminado
    path('eliminarCultivo/<nombre>', views.eliminarCultivo),
    #path to wiki function at views
    path('wiki/', views.wiki),
    #path to read function indexed with wiki at views
    path('read/', views.read),
    
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

