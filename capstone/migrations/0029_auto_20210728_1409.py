# Generated by Django 3.1.1 on 2021-07-28 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0028_listing_trailer'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='img',
            field=models.CharField(blank=True, default=None, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='imgg',
            field=models.CharField(blank=True, default=None, max_length=64, null=True),
        ),
    ]
