# Generated by Django 2.2.6 on 2019-10-23 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debadmin', '0002_adminemail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminuser',
            name='user_type_id',
            field=models.IntegerField(),
        ),
    ]
