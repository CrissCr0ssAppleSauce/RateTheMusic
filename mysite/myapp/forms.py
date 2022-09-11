from django import forms

from . import models
from django.utils.safestring import mark_safe

class ArtistForm(forms.Form):
    name = forms.CharField(label="Artist Name ",required=True,max_length=240)
    artist_pic = forms.ImageField(label="Artist Picture ", required=True)
    def save(self):
        artist_instance = models.Artist()
        artist_instance.name = self.cleaned_data["name"]
        artist_instance.artist_pic = self.cleaned_data["artist_pic"]
        artist_list = models.Artist.objects.all()
        artist_instance.artist_id = len(artist_list)+1
        artist_instance.avg_rating_art = 0;
        artist_instance.avg_rating_art_round = 0;
        artist_instance.save()
        return artist_instance

class AlbumForm(forms.Form):
    album_name = forms.CharField(label="Name ", required=True, max_length=240)
    album_cover = forms.ImageField(label="Cover ", required=True)

    def save(self, ID):
        album_instance = models.Album()
        album_instance.name = self.cleaned_data["album_name"]
        album_instance.artist = models.Artist.objects.get(artist_id=ID)
        artist_obj = models.Artist.objects.get(artist_id=ID)
        albums_list = artist_obj.album_set.all()
        album_instance.album_id = len(models.Artist.objects.all())+1
        album_instance.album_cover = self.cleaned_data["album_cover"]
        album_instance.avg_rating_alb = 0;
        album_instance.avg_rating_alb_round = 0;
        album_instance.save()
        return album_instance

class ReviewForm(forms.Form):


    rating = forms.CharField(label='Rating', required=True, widget=forms.RadioSelect(choices=[
        (1, ''),
        (2, ''),
        (3, ''),
        (4, ''),
        (5, ''),
        ], attrs={'class': 'rt'}),

        )
    username = forms.CharField(label="Name ", required=True, max_length=240, widget=forms.TextInput(attrs={'id': 'name'}))
    review_msg = forms.CharField(label="Review ", required=True, widget=forms.Textarea)

    def save(self, pk2):
        review_instance = models.ReviewModel()
        review_instance.username = self.cleaned_data["username"]
        review_instance.review_msg = self.cleaned_data["review_msg"]
        review_instance.rating = self.cleaned_data["rating"]
        review_instance.album = models.Album.objects.get(album_id=pk2)
        review_instance.save()
        return review_instance
