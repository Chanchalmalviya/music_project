from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.views import View

# Create your views here.

def song_list(request):
      song = NewSong.objects.all()
      return render(request,'music/song_list.html',{'song':song})

def add_song(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        artist = request.POST.get('artist')
        album = request.POST.get('album')
        file = request.FILES['file']
        NewSong.objects.create(title=title, artist=artist, album=album, file=file)
        return redirect('/')
    return render(request, 'music/add_song.html')


def delete_song(request, pk):
    song = NewSong.objects.get(id=pk)
    if request.method == 'POST':
        song.delete()
        return redirect('/')
    return render(request, 'music/delete_song.html', {'song': song})


def update_view(request, pk):
    song = NewSong.objects.get(id=pk)
    
    return render(request, 'music/update_song.html', {'song': song})

def update_song(request):
    
    if request.method == 'POST':
        pk = request.POST['pk']
        title = request.POST.get('title')
        artist = request.POST.get('artist')
        album = request.POST.get('album')
        file = request.FILES.get('file')
        song_obj = NewSong.objects.get(id=pk)
        song_obj.title=title
        song_obj.artist=artist
        song_obj.album=album
        if file:
            song_obj.file=file
        song_obj.save()
   # NewSong.objects.create(title=title, artist=artist, album=album, file=file)
        return redirect('/')
    

def play_song(request, pk):
    song = NewSong.objects.filter(id=pk)
    #return HttpResponse(f'Now playing: {song.title}') 
    return render(request, 'music/play_song.html', {'song': song})  


     