# Generated by Django 2.2.6 on 2019-10-29 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debadmin', '0041_auto_20191029_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='created_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='modified_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='modified_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_status',
            field=models.CharField(default='active', max_length=8),
        ),
        migrations.AddField(
            model_name='product',
            name='shipping_dimension_class',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='shipping_product_height',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='shipping_product_length',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='shipping_product_width',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='link',
            field=models.TextField(null=True),
        ),
    ]
