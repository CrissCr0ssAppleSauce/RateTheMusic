# Generated by Django 3.1.6 on 2021-05-18 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_album_avg_rating_alb_round'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='avg_rating_art',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='avg_rating_art_round',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]