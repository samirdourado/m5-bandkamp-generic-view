# Generated by Django 4.0.7 on 2023-04-20 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0003_alter_song_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='song',
            options={'ordering': ('id',)},
        ),
    ]
