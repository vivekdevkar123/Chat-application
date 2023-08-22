from django.shortcuts import render,redirect
from .models import Group,Chat
# Create your views here.

def home(request):
    if(request.method == 'POST'):
        group_name = request.POST.get('group_name')
        group = Group.objects.filter(group_name = group_name).first()

        if not group:
            group = Group(group_name = group_name)
            group.save()

        return redirect('index',group_name=group_name)
    
    return render(request,'app/home.html')

def index(request,group_name):
    group = Group.objects.get(group_name = group_name)
    chats = Chat.objects.filter(group = group)
    return render(request,'app/index.html',{'groupname':group_name,'chats':chats})