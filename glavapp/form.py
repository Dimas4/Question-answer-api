from django import forms
from .models import Message

class NewSendForm(forms.ModelForm):
    user = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Введите Ваше ФИО'
        }
    ))
    message = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Введите Ваше сообщение'
        }
    ))
    class Meta:
        model = Message
        fields = ['user', 'message']