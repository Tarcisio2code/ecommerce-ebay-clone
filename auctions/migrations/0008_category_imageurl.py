# Generated by Django 4.1.1 on 2022-12-22 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='imageUrl',
            field=models.CharField(blank=True, default=None, max_length=1000, null=True),
        ),
    ]
