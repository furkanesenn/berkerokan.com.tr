# Generated by Django 5.0.1 on 2024-02-09 19:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('object_id', models.PositiveIntegerField()),
                ('author', models.CharField(max_length=200, verbose_name='Yorumun Sahibi')),
                ('author_email', models.EmailField(max_length=200, verbose_name='Yorumun Sahibinin E-Posta Adresi')),
                ('body', models.TextField(verbose_name='Yorumun İçeriği')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')),
                ('like_count', models.IntegerField(default=0, editable=False, verbose_name='Beğeni Sayısı')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'Yorum',
                'verbose_name_plural': 'Yorumlar',
                'ordering': ['-created_at'],
            },
        ),
    ]
