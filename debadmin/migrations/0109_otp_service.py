# Generated by Django 2.2.6 on 2019-12-12 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debadmin', '0108_auto_20191210_1325'),
    ]

    operations = [
        migrations.CreateModel(
            name='otp_service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.IntegerField(null=True)),
                ('otp', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
