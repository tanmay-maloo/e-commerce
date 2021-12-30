# Generated by Django 3.0.3 on 2021-12-30 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_product_average_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='total_ratings_sum',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='total_reviews',
            field=models.IntegerField(default=0),
        ),
    ]