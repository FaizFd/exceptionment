# Generated by Django 3.1.1 on 2021-06-14 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0002_listing_categorys'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='links',
            field=models.CharField(blank=True, default=None, max_length=64, null=True),
        ),
    ]
