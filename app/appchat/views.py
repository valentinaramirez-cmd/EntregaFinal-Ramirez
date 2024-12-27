from django.shortcuts import redirect, render
from django.views.generic import DetailView, CreateView, DeleteView, ListView, UpdateView

from .forms import ChatRoomForm, MensajeForm
from .models import ChatRoom, Mensaje

# Create your views here.

class CreateMensajeView(CreateView): 
    model = Mensaje 
    fields = ('mensaje')
    template = './templates/appchat/mensaje_form.html'

class DetailMensajeView(DetailView): 
    model = Mensaje
    template_name = './templates/appuser/mensaje.html'
    context_object_name = 'mensaje'


def ver_rooms(request): 
    rooms = ChatRoom.objects.all()
    return render(request, './appchat/ver_rooms.html', {'rooms' : rooms})

    

def enterRoom (request): 
    form = ChatRoomForm(request.POST)
    
    if ChatRoom.objects.filter(nombre= form.fields['nombre']).exists():
        return redirect('room/' + form.fields['nombre'])
    else: 
        if form.is_valid(): 
            form.save()
        else: 
            form = ChatRoomForm() 

    return render(request, './appchat/enter_room.html', {'form' : form})


def chatRoom (request, room): 
    room = ChatRoom.objects.filter(nombre = room).values()

    return render(request, './appchat/chat_room.html', {'room' : room})


def enviarMensaje (request, room):
    chat = ChatRoom.objects.filter(nombre = room).values() 
    if request.method == 'POST': 
        form = MensajeForm(request.POST)

        if form.is_valid(): 
            chat.mensajes.append(form)
            chat.save()
            ##refresh auto 
        else: 
            form = MensajeForm()

    return render(request, './templates/appchat/chat_room.html', {'form' : form})