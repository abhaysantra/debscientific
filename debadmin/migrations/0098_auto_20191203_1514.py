# Generated by Django 2.2.6 on 2019-12-03 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debadmin', '0097_order_details_addon_product_id_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addon_order',
            name='addon_product_id_list',
        ),
        migrations.AddField(
            model_name='addon_order',
            name='addon_product_id',
            field=models.IntegerField(null=True),
        ),
    ]