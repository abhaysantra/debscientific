# Generated by Django 2.2.6 on 2019-12-12 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debadmin', '0109_otp_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp_service',
            name='otp',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='otp_service',
            name='phone_number',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
