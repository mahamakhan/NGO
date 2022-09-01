# Generated by Django 3.2.12 on 2022-09-01 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NgoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=120)),
                ('zakat_eligible', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Donations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('typeof', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=400)),
                ('injured_reserved_list', models.BooleanField()),
                ('ngo_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donations', to='ngo.ngolist')),
            ],
        ),
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('iban', models.IntegerField()),
                ('donation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bank_account', to='ngo.donations')),
            ],
        ),
    ]
