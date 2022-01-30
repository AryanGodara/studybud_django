from multiprocessing import context
from django.shortcuts import render, redirect

from .models import Room
from .forms import RoomForm

# Create your views here.


def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)


def room(request,pk):
    room = Room.objects.get(id=pk)

    context = {'room': room}
    return render(request, 'base/room.html', context)


def createRoom(request):
    form = RoomForm()
    
    if request.method == 'POST':
        # print(request.POST)     #? request.POST is the 'query/list' containg the form data filled by the user
        form = RoomForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('home') # We can enter 'home' instead of absolute path, because of name="home" in urls.py
    
    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)   #? So that the form is pre-filled with the current values
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
            #? If we don't specify instance=room, it'll create a NEW room, instead of updating the values of the correct room
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form':form}
    return render(request, 'base/room_form.html', context)