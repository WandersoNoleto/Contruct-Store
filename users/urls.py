from django.urls import path

from . import views

urlpatterns = [
    path('cadastrar-vendedor/', views.cadastrar_vendedor, name='cadastrar_vendedor'),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout")
]
