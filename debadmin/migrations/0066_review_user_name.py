# Generated by Django 2.2.6 on 2019-11-07 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debadmin', '0065_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='user_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]