# Generated by Django 3.2.12 on 2022-09-08 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0008_alter_donations_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngolist',
            name='profit',
            field=models.CharField(max_length=1020, null=True),
        ),
    ]