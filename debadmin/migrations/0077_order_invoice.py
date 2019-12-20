# Generated by Django 2.2.6 on 2019-11-13 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debadmin', '0076_remove_user_cart_item_cart_session_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='order_invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(null=True)),
                ('order_id', models.IntegerField(null=True)),
                ('invoice', models.ImageField(null=True, upload_to='generated_invoice')),
                ('barcode', models.ImageField(null=True, upload_to='barcode')),
                ('created_date', models.DateField(null=True)),
            ],
        ),
    ]