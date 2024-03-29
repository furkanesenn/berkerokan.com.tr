# Generated by Django 5.0.1 on 2024-02-09 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_book_rating_book_rating_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, editable=False, max_digits=2, null=True, verbose_name='Değerlendirme Puanı (5 üzerinden - Site İçi)'),
        ),
    ]
