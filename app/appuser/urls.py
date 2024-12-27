from django.urls import path

from .views import DeleteUserView, DetailUserView, LoginUserView, RegisterUserView, UpdateUserView, get_user

app_name = 'appuser'

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'), 
    path('login/', LoginUserView.as_view(), name='login'),
    path('update_user/<int:pk>', UpdateUserView.as_view(), name='update_user'), 
    path('delete_user/<int:pk>', DeleteUserView.as_view(), name='delete_user'), 
    path('ver_perfil/<int:pk>', DetailUserView.as_view(), name='detail_user'), 
    path('lista/', get_user, name='lista')
] 

