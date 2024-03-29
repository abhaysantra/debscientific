# Generated by Django 2.2.6 on 2019-10-29 11:30

from django.db import migrations, models
import django_resized.forms
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('debadmin', '0042_auto_20191029_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_image',
            name='product_details',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, null=True, quality=0, size=[1920, 1080], upload_to='product_details'),
        ),
        migrations.AlterField(
            model_name='product_image',
            name='product_list',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to='product_list'),
        ),
        migrations.AlterField(
            model_name='video',
            name='link',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
