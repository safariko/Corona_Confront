# Generated by Django 2.2.12 on 2020-04-09 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0005_remove_reimburse_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='insurance_exists',
            field=models.CharField(choices=[('NO', 'No'), ('YES', 'Yes')], default='NO', max_length=3),
        ),
    ]
