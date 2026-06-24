from django.urls import path
from . import views
from cadastro_usuario import views as cadastro_views
urlpatterns = [
    path('back-end/templates/login.html', views.login, name='login'),
]
