# Generated by Django 4.1.1 on 2022-09-28 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=255)),
                ('has_requested', models.BooleanField(default=False)),
                ('request_status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_index', models.CharField(max_length=255)),
                ('asset_status', models.BooleanField(default=False)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.account')),
            ],
        ),
    ]
