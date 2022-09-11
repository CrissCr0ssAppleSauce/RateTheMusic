from django.db import models


# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=240)
    artist_id = models.IntegerField(null=True);
    artist_pic = models.FileField(upload_to='images', null=True, blank=True)
    avg_rating_art = models.FloatField(null=True,blank=True)
    avg_rating_art_round = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.name

    def get_ratings(self):
        rating = 0
        total_num_ratings = 0
        albums = self.album_set.all()
        for album in albums:
            reviews = album.reviewmodel_set.all()
            for review in reviews:
                rating += review.rating
            num_ratings = album.get_num_ratings()
            total_num_ratings += num_ratings
        if total_num_ratings > 0:
            self.avg_rating_art = rating / total_num_ratings
            self.avg_rating_art_round = round(self.avg_rating_art)

class Album(models.Model):
    name = models.CharField(max_length=240)
    album_id = models.IntegerField(null=True);
    #artist_name = models.CharField(max_length=240)
    artist = models.ForeignKey(Artist, null=True, on_delete=models.SET_NULL)
    album_cover = models.FileField(upload_to='images',null=True, blank=True)
    avg_rating_alb = models.FloatField(null=True,blank=True)
    avg_rating_alb_round = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.name
    def get_ratings(self):
        reviews = self.reviewmodel_set.all()
        rating = 0;
        for review in reviews:
            rating += int(review.rating)
        if len(reviews) > 0:
            self.avg_rating_alb = rating / len(reviews)
            self.avg_rating_alb_round = round(self.avg_rating_alb)
    def get_num_ratings(self):
        reviews = self.reviewmodel_set.all()
        return len(reviews)

class ReviewModel(models.Model):
    rating = models.IntegerField(null=True)
    review_msg = models.TextField(null=True)
    username = models.CharField(max_length=240)

    album = models.ForeignKey(Album, null=True, on_delete=models.SET_NULL)

class MessageModel(models.Model):
    sender = models.TextField()
    message_text = models.TextField()
    time = models.TextField(null=True)
    artist = models.ForeignKey(Artist, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.sender

    def recent_messages(self):
        #return MessageModel.objects.order_by('-time').all()[:50]
        return MessageModel.objects.order_by('time').all()[:50]
