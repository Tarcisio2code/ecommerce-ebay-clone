# Generated by Django 4.1.1 on 2022-12-27 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_category_imageurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
