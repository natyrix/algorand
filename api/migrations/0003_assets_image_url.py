# Generated by Django 4.1.1 on 2022-09-29 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_account_is_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='assets',
            name='image_url',
            field=models.CharField(default='None', max_length=255),
        ),
    ]
