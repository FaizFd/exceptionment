# Generated by Django 3.1.1 on 2021-07-17 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0007_listing_cast'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='cast',
            field=models.TextField(default=None, max_length=1000, null=True),
        ),
    ]
