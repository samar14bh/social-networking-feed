from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Room, Topic,User
from django.db.models import Q
from .forms import RoomForm
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout 
from django.contrib.auth.decorators import login_required
#create function and methods
"""rooms=[
    {'id':1, 'name':'room1'},
    {'id':2, 'name':'room2'},
    {'id':3, 'name':'room3'},
]"""


def loginPage(request):    
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user=User.objects.get(username=user)
        except:
            messages.error(request,'User does not exist')
        user=authenticate(request,username=username,password=password)  
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Username OR password does not exist')
    context={}
    return render(request, 'base/login_register.html',context)
def logoutUser(request):
    logout(request)
    return redirect('home')  

def home(request):
    q=request.GET.get('q') if request.GET.get('q')!=None else '' 
    #get the query from the url
    rooms=Room.objects.filter(Q(topic__name__icontains=q)|Q(name__icontains=q)|Q(description__icontains=q))#filter the rooms by the query
    #the request us the http sent to the api 
    topics=Topic.objects.all()
    room_count= rooms.count()
    context={'rooms':rooms,'topics':topics,'room_count':room_count}
    return  render(request, 'base/home.html', context)


#room functions
def room(request, pk):
    room=Room.objects.get(id=pk)
    context ={'room':room}
    return render(request, 'base/room.html',context)
@login_required(login_url='login')
def createRoom(request):
    form=RoomForm()
    if request.method=='POST':
       form=RoomForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('home')
    context={'form':form}
    return render(request, 'base/room_form.html',context)

def updateRoom(request,pk):
    room=Room.objects.get(id=pk)
    form=RoomForm(instance=room)#prefill the form with existing data 
    if request.method=='POST':
       form=RoomForm(request.POST,instance=room)
       if form.is_valid():
           form.save()
           return redirect('home')
    context={'form':form}
    return render(request, 'base/room_form.html',context)

def deleteRoom(request,pk):
    room=Room.objects.get(id=pk)
    if request.method=='POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'object':room})

#topic functions
