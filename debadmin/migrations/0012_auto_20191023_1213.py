# Generated by Django 2.2.6 on 2019-10-23 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debadmin', '0011_auto_20191023_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='created_by',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='slider',
            name='modified_by',
            field=models.IntegerField(default=None),
        ),
    ]
