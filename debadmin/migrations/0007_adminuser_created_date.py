# Generated by Django 2.2.6 on 2019-10-23 06:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('debadmin', '0006_auto_20191023_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminuser',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]