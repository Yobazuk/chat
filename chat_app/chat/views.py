from django.shortcuts import render
from .models import Message


def index(request):
    return render(request, 'chat/index.html')


def chatroom(request):
    username = request.GET.get('username', 'Unknown')
    messages = Message.objects.all()

    return render(request, 'chat/chatroom.html', {'username': username, 'messages': messages})
