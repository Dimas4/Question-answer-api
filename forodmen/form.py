from django import forms
from glavapp.models import Message

class NewSendForm(forms.ModelForm):
    answer = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Введите здесь текст'
        }
    ))
    class Meta:
        model = Message
        fields = ['answer']