# Generated by Django 5.0.1 on 2024-02-08 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_book_created_at_book_impression_count_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-created_at'], 'verbose_name': 'Kitap', 'verbose_name_plural': 'Kitaplar'},
        ),
        migrations.RemoveField(
            model_name='book',
            name='impression_count',
        ),
        migrations.AddField(
            model_name='book',
            name='engagement_count',
            field=models.IntegerField(default=0, editable=False, verbose_name='Etkileşim Sayısı'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=200, verbose_name='Yazar'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(upload_to='covers/', verbose_name='Kapak Fotoğrafı'),
        ),
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi'),
        ),
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Yayın Tarihi'),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Açıklama'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Tür'),
        ),
        migrations.AlterField(
            model_name='book',
            name='keywords',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Anahtar Kelimeler'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Fiyat'),
        ),
        migrations.AlterField(
            model_name='book',
            name='purchase_link',
            field=models.URLField(blank=True, null=True, verbose_name='Satın Alma Linki'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=200, unique=True, verbose_name='Ad'),
        ),
        migrations.AlterField(
            model_name='book',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi'),
        ),
        migrations.AlterField(
            model_name='book',
            name='view_count',
            field=models.IntegerField(default=0, editable=False, verbose_name='Görüntülenme Sayısı'),
        ),
    ]
