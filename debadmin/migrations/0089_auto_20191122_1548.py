# Generated by Django 2.2.6 on 2019-11-22 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debadmin', '0088_product_product_specification'),
    ]

    operations = [
        migrations.CreateModel(
            name='sub_product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(null=True)),
                ('sub_product_name', models.CharField(max_length=255, null=True)),
                ('sub_product_price', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('sub_product_desc', models.TextField(null=True)),
                ('status', models.CharField(default='active', max_length=8)),
                ('created_date', models.DateField(null=True)),
                ('created_by', models.IntegerField(null=True)),
                ('modified_date', models.DateField(null=True)),
                ('modified_by', models.IntegerField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='adminuser',
            name='gst_no',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='billing_address',
            name='gst_no',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='user_address',
            name='gst_no',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
