# Generated by Django 3.0.3 on 2021-12-31 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0030_auto_20211231_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewrating',
            name='review_images',
            field=models.ImageField(blank=True, upload_to='images/reviews'),
        ),
        migrations.DeleteModel(
            name='ReviewRatingImages',
        ),
    ]
