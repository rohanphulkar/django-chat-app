from django.shortcuts import render,redirect,HttpResponse
from .models import Room,Chat
from accounts.models import User
from django.db.models import Q
import datetime
# Create your views here.
def inbox(request):
    if request.user.is_authenticated:
        rooms = Room.objects.filter(Q(owner=request.user)|Q(user=request.user))
        return render(request, 'chat/inbox.html',{"rooms":rooms})
    else:
        return redirect('login')

def chat(request,id):
    if request.user.is_authenticated:
        room = Room.objects.filter(id=id)
        if room:
            room=room.first()
            username = room.user.username
            cur_user = request.user
            chat = Chat.objects.filter(room=id)
            return render(request, 'chat/chat.html',{"chats":chat,"username":username,"room_name":room,"cur_user":str(cur_user)})
        else:
            return redirect('inbox')
    else:
        return redirect('login')
    
def searchUsers(request):
    if request.user.is_authenticated:
        if request.method=="GET":
            query = request.GET.get('search',None)
            if query is None:
                users = User.objects.all().exclude(id = request.user.id)
            else:
                users = User.objects.filter(username__icontains=query)
            return render(request,'chat/allusers.html',{"users":users})
    else:
        return redirect('login')

def createRoom(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            userId = request.POST.get('userId')
            user = User.objects.get(id=userId)
            room  = Room.objects.create(user=user,owner=request.user)
            return redirect('inbox')
        else:
            return redirect('search')
    else:
        return redirect('login')
            