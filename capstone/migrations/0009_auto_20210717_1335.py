# Generated by Django 3.1.1 on 2021-07-17 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capstone', '0008_auto_20210717_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='cast',
            field=models.TextField(),
        ),
    ]
