# Generated by Django 5.0.1 on 2024-02-09 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_alter_book_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=0.0, editable=False, max_digits=3, verbose_name='Değerlendirme (Site İçi)'),
        ),
    ]