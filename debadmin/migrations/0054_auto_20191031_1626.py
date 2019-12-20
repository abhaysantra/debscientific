# Generated by Django 2.2.6 on 2019-10-31 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debadmin', '0053_auto_20191031_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_cart_item',
            name='cart_item_qty',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='mrp_price',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sell_price',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='user_cart_item',
            name='cart_discount',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='user_cart_item',
            name='cart_mrp_price',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='user_cart_item',
            name='cart_sell_price',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
    ]