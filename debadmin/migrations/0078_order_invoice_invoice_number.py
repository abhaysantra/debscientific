# Generated by Django 2.2.6 on 2019-11-15 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debadmin', '0077_order_invoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_invoice',
            name='invoice_number',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
