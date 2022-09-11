from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import models
from .forms import ReviewForm
from .forms import AlbumForm
from .forms import ArtistForm

import PIL

# from . import forms
# Create your views here.
def index(request):

    if request.method == "POST":
        form = ArtistForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form = ArtistForm()
            return HttpResponseRedirect("/")
    else:
        form = ArtistForm()

    artist_objects = models.Artist.objects.all()

    for artist in artist_objects:
        artist.get_ratings()

    context = {
        "title": "Rate the Music",
        "variable": "Main Page",
        "artists": artist_objects,
        "artist_form": form,
    }

    return render(request, "index.html", context=context)

def artist_index(request, pk):
    if request.method == "POST":
        form = AlbumForm(request.POST,request.FILES)
        if form.is_valid():
            form.save(pk)
            form = AlbumForm()
            return HttpResponseRedirect("/Artist/" + str(pk))
    else:
        form = AlbumForm()

    artist_obj = models.Artist.objects.get(artist_id=pk)
    albums_list = artist_obj.album_set.all()
    for album in albums_list:
        album.get_ratings()
    artist_obj.get_ratings()
    rating = artist_obj.avg_rating_art



    context = {
        "artist_header": artist_obj.name,
        "albums": albums_list,
        "artist_id": pk,
        "album_form": form,
        "average": round(rating),
        "actual_avg": format(rating, '.2f'),
    }
    return render(request, "artist_page.html", context)

def room(request, pk, room_name):
    return render(request, 'chat_room.html', {
        'room_name': room_name
    })

def album_index(request, pk1, pk2):

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save(pk2)
            form = ReviewForm()
            return HttpResponseRedirect("/Artist/" + str(pk1) + "/Album/" + str(pk2))
    else:
        form = ReviewForm()

    album_obj = models.Album.objects.get(album_id=pk2)
    reviews = album_obj.reviewmodel_set.all()
    album_obj.get_ratings()
    rating = album_obj.avg_rating_alb;

    context = {
        "album_header": album_obj.name,
        "review_form": form,
        "reviews": reviews,
        "average": round(rating),
        "actual_avg": rating,
    }
    return render(request, "album_page.html", context)
