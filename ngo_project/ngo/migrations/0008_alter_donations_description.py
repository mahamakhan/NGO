# Generated by Django 3.2.12 on 2022-09-07 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0007_rename_city_ngolist_founded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donations',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
