# Generated by Django 2.2.6 on 2019-11-05 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debadmin', '0062_enquiry_order_order_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminuser',
            name='landmark',
            field=models.CharField(max_length=255, null=True),
        ),
    ]