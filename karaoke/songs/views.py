from django.shortcuts import get_object_or_404, render
from .models import Song, Performer


def home(request):
    return render(request, 'home.html')

def song_list(request):
    songs = Song.objects.all()
    return render(request, 'songs/song_list.html', {'songs': songs})

def song_detail(request, song_pk):
    song = get_object_or_404(Song, pk=song_pk)
    return render(request, 'songs/song_detail.html', {'song': song})

def performer_detail(request, performer_pk):
    performer = get_object_or_404(Performer, pk=performer_pk)
    songs = Song.objects.filter(performer=performer)
    print(performer)
    return render(request, 'songs/performer_detail.html', {'performer': performer, 'songs': songs})
