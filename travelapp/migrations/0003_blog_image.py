# Generated by Django 3.1.4 on 2020-12-30 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_place_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default=0, upload_to='blogs'),
            preserve_default=False,
        ),
    ]