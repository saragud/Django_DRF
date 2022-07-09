# Generated by Django 4.0.4 on 2022-05-27 16:19

from django.db import migrations, models
import eshop_products.models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0002_product_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=eshop_products.models.upload_image_path, verbose_name='تصویر'),
        ),
    ]