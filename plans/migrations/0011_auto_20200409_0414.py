# Generated by Django 2.2.12 on 2020-04-09 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0010_auto_20200409_0139'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='insurance_no',
            field=models.BooleanField(default=False, verbose_name='No'),
        ),
        migrations.AddField(
            model_name='customer',
            name='insurance_yes',
            field=models.BooleanField(default=False, verbose_name='Yes'),
        ),
    ]
