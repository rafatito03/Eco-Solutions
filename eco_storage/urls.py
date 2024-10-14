from django.urls import path
from usuarios import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logout/', views.user_logout, name='logout'),
    path('home/', views.home, name='home'),
    path('',views.mapa,name='mapa'),
]
