from django import forms

from .models import ChatRoom, Mensaje

class ChatRoomForm(forms.ModelForm): 
    class Meta: 
        model= ChatRoom 
        fields= ['nombre']

class MensajeForm(forms.ModelForm): 
    class Meta: 
        model = Mensaje 
        fields = ['mensaje']