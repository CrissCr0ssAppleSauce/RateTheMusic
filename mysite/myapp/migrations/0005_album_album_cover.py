# Generated by Django 3.1.6 on 2021-05-15 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_messagemodel_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='album_cover',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
