# Generated by Django 2.2.6 on 2019-12-09 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debadmin', '0099_countries'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countries',
            name='name',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
