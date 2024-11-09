from django.urls import path
from usuarios import views
from django.contrib import admin

urlpatterns = [
    path('admin/',admin.site.urls),
    path('login/', views.user_login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logout/', views.user_logout, name='logout'),
    path('home/', views.home, name='home'),
    path('mapa/',views.mapa,name='mapa'),
    path('ong/<int:pk>/', views.verificar_ong, name='ong_detail'),
    path('ong/<int:ong_id>/update/', views.update_ong, name='update_ong'),
]
