# Generated by Django 3.0.5 on 2020-07-07 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_auto_20200707_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='date',
            field=models.DateField(null=True),
        ),
    ]