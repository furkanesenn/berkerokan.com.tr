# Generated by Django 5.0.1 on 2024-01-31 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('cover', models.ImageField(blank=True, upload_to='covers/')),
                ('genre', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('purchase_link', models.URLField()),
            ],
        ),
    ]
