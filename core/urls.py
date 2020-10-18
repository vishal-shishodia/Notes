from django.urls import path
from django.contrib.auth.views import LoginView
from .views import *

urlpatterns = [
    path('', index,name='index'),
    path('user_home', UserHome,name='user_home'),
    path('register/', Register,name='register'),
    path('add_note/', AddNote,name='add_note'),
    path('update_note/<str:pk>/', UpdateNote,name='update_note'),
    path('delete_note/<str:pk>/', DeleteNote,name='delete_note'),
    path('detail_note/<str:pk>/', DetailNote,name='detail_note'),
    path('login/',LoginView.as_view(template_name='core/login.html'),name='login'),
    path('login_success/',LoginSuccess,name='login_success'),
    path('logout/',LogOut,name='logout'),
    path('admin_home/', AdminHome,name='admin_home'),
]