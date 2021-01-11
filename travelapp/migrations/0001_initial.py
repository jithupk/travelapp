# Generated by Django 3.1.4 on 2020-12-30 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.ImageField(upload_to='')),
                ('month', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=50)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('price', models.FloatField()),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]