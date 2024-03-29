# Generated by Django 2.2.6 on 2019-10-24 05:57

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('debadmin', '0018_auto_20191024_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', django_resized.forms.ResizedImageField(crop=None, default=None, force_format=None, keep_meta=True, quality=0, size=[600, 600], upload_to='gallery')),
                ('status', models.CharField(default='active', max_length=8)),
                ('created_date', models.DateField(default=None)),
                ('created_by', models.IntegerField(default=None)),
                ('modified_date', models.DateField(default=None)),
                ('modified_by', models.IntegerField(default=None)),
            ],
        ),
    ]
