# Generated by Django 2.2.6 on 2019-10-29 05:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('debadmin', '0040_auto_20191029_1115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product_download_image',
            old_name='modifiedd_date',
            new_name='modified_date',
        ),
        migrations.RenameField(
            model_name='product_image',
            old_name='modifiedd_date',
            new_name='modified_date',
        ),
    ]
