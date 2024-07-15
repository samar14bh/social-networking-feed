from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
#create function and methods
"""rooms=[
    {'id':1, 'name':'room1'},
    {'id':2, 'name':'room2'},
    {'id':3, 'name':'room3'},
]"""


def home(request):
    #the request us the http sent to the api 
    rooms=Room.objects.all()#import all of them from db
    context={'rooms':rooms}
    return  render(request, 'base/home.html', context)
def room(request, pk):
    room=Room.objects.get(id=pk)
    context ={'room':room}
    return render(request, 'base/room.html',context)

def createRoom(request):
    context={}
    return render(request, 'base/room_form.html',context)