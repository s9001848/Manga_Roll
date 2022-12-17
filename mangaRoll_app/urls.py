from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_manga/', views.add_manga, name='add_manga'),
    path('view_mangas/', views.view_mangas, name='view_manga'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('manger_registration/', views.manger_registration, name='manger_registration'),
    path('change_password/', views.change_password, name='change_password'),
    path('manger_login/', views.manger_login, name='manger_login'),
    path('logout/', views.logout, name='logout'),
    path('delete_manga/<int:myid>/', views.delete_manga, name='delete_manga'),
    path('delete_user/<int:myid>/', views.delete_user, name='delete_user'),
    # path('create_chat/', views.create_chat, name='create_chat'),
    # path('list_chat/', views.list_chat, name='list_chat'),
]