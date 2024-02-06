# Generated by Django 5.0.1 on 2024-02-04 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('short_description', models.TextField()),
                ('article_type', models.CharField(choices=[('Dizi Hikayeler', 'Dizi Hikayeler'), ('Öyküler', 'Öyküler'), ('Denemeler', 'Denemeler'), ('Kaynak Tavsiyeleri', 'Kaynak Tavsiyeleri'), ('Kitap Yorumları', 'Kitap Yorumları')], default='Dizi Hikayeler', max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('cover', models.ImageField(upload_to='article_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('like_count', models.IntegerField(default=0)),
                ('view_count', models.IntegerField(default=0)),
            ],
        ),
    ]