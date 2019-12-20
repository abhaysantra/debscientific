# Generated by Django 2.2.6 on 2019-10-24 12:34

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('debadmin', '0025_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='valuableCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=255)),
                ('customer_image', django_resized.forms.ResizedImageField(crop=None, default=None, force_format=None, keep_meta=True, quality=0, size=[100, 100], upload_to='valuable_customer')),
                ('status', models.CharField(default='active', max_length=8)),
                ('created_date', models.DateField(default=None)),
                ('created_by', models.IntegerField(default=None)),
                ('modified_date', models.DateField(default=None)),
                ('modified_by', models.IntegerField(default=None)),
            ],
        ),
    ]
