# Generated by Django 2.2.6 on 2019-11-25 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debadmin', '0089_auto_20191122_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='sub_category',
            field=models.IntegerField(null=True),
        ),
    ]
