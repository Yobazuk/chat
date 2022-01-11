from django.shortcuts import render


def index(request):
    return render(request, 'chat/index.html')


def chatroom(request):
    username = request.GET.get('username', 'Unknown')
    return render(request, 'chat/chatroom.html', {'username': username})
