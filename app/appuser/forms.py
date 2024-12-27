from django import forms 
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User

class UserCreationForm(UserCreationForm): 
    class Meta: 
        model = User 
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'email')
        widgets = {
            'fecha_nacimiento' : forms.DateInput(attrs={'type' : 'date'})
        }

class UpdateUserForm (UserChangeForm):
    password = None 
    class Meta: 
        model = User
        fields = ('username', 'first_name', 'email')
        
