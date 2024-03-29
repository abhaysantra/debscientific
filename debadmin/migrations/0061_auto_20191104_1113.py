# Generated by Django 2.2.6 on 2019-11-04 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debadmin', '0060_billing_address_order_address_user_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='billing_address',
            name='created_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='order_address',
            name='bill_address_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user_address',
            name='created_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user_address',
            name='modified_by',
            field=models.IntegerField(null=True),
        ),
    ]
