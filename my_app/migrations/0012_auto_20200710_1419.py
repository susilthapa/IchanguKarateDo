# Generated by Django 3.0.5 on 2020-07-10 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0011_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='fb_link',
            field=models.URLField(blank=True, unique=True, verbose_name='Facebook Link'),
        ),
        migrations.AddField(
            model_name='contact',
            name='insta_link',
            field=models.URLField(blank=True, unique=True, verbose_name='Instagram Link'),
        ),
        migrations.AddField(
            model_name='contact',
            name='youtube_link',
            field=models.URLField(blank=True, unique=True, verbose_name='Youtube Link'),
        ),
    ]
