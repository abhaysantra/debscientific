# Generated by Django 2.2.6 on 2019-10-25 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('debadmin', '0028_category_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='sub_category',
        ),
    ]
