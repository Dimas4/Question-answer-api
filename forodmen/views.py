from django.shortcuts import render, get_object_or_404
from glavapp.models import Message
from django.http import HttpResponseRedirect, HttpResponse
from .form import NewSendForm



def home(request):
    if not request.user.is_staff or not request.user.is_superuser:
        return HttpResponse(status=404)
    new = Message.objects.all()
    form = NewSendForm(request.POST or None)
    send = {
        'new': new,
        'form': form
    }
    return render(request, "home/new.html", send)

def send(request, pk):
    new = get_object_or_404(Message, pk=pk)
    form = NewSendForm(request.POST or None, instance=new)
    if form.is_valid():
        sav = form.save(commit=False)
        sav.save()

    al = Message.objects.all()

    send = {
        'new': al,
        'form': form,
    }

    return HttpResponseRedirect('/ad/')

def delete(request, pk):
    new = get_object_or_404(Message, pk=pk)
    new.delete()

    al = Message.objects.all()
    send = {
        'new': al,
    }

    return HttpResponseRedirect('/ad/')





