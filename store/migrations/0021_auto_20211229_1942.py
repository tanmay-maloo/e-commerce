# Generated by Django 3.0.3 on 2021-12-29 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_auto_20211229_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewrating',
            name='review_images',
            field=models.ImageField(blank=True, upload_to='images/reviews'),
        ),
    ]