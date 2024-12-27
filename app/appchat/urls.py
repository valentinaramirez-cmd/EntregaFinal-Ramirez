from django.urls import path

from .views import enterRoom, chatRoom, ver_rooms

app_name = 'appchat'

urlpatterns = [
    path('room/<str:room>', chatRoom, name='chatRoom'), 
    path('enterRoom/', enterRoom, name='enterRoom'),
    path('ver_rooms/', ver_rooms, name='ver_rooms')
]