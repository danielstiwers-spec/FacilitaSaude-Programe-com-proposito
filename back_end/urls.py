from django.urls import path
from . import views

urlpatterns = [
    path('login.html', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_usuario, name='cadastro'),
    path('user-cadastrado/', views.user_cadastrado_view, name='user_cadastrado'),
]
