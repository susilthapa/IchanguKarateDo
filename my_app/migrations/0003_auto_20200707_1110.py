# Generated by Django 3.0.5 on 2020-07-07 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_auto_20200707_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='slug',
            field=models.SlugField(default='', editable=False, unique=True),
        ),
    ]
