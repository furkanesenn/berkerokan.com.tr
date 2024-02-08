# Generated by Django 5.0.1 on 2024-02-08 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_posted_at', models.DateTimeField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('subscriber_count', models.IntegerField(default=0, editable=False)),
                ('newsletter_stats', models.JSONField(blank=True, editable=False, null=True)),
            ],
        ),
    ]