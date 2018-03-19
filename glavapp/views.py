from django.shortcuts import render
from .form import NewSendForm
from .models import Message
from django.http import HttpResponseRedirect


def home(requset):

    form = NewSendForm(requset.POST or None)

    if form.is_valid():
        new = form.save()
        new.save()
        return HttpResponseRedirect('/')

    mod = Message.objects.all().order_by('-data_new')

    send = {
        'form': form,
        'mod': mod
    }
    return render(requset, "home/gl.html", send)
