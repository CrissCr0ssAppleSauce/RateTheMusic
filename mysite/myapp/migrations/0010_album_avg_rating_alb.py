# Generated by Django 3.1.6 on 2021-05-18 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_remove_reviewmodel_stars'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='avg_rating_alb',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
