# Generated by Django 2.2.6 on 2019-10-25 07:44

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('debadmin', '0033_auto_20191025_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_commission_fixed',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_commission_percent',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, null=True, quality=0, size=[250, 250], upload_to='category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_meta_description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_meta_keyword',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_meta_title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_slug',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent_category',
            field=models.IntegerField(null=True),
        ),
    ]
