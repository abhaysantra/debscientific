# Generated by Django 2.2.6 on 2019-11-19 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debadmin', '0079_order_details_return_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_details',
            name='return_status',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
