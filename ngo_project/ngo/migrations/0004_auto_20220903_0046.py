# Generated by Django 3.2.12 on 2022-09-03 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo', '0003_auto_20220902_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='iban',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='bankaccount',
            name='number',
            field=models.CharField(max_length=100),
        ),
    ]
