# Generated by Django 2.2.6 on 2019-12-09 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debadmin', '0104_states'),
    ]

    operations = [
        migrations.AddField(
            model_name='states',
            name='auto_id',
            field=models.IntegerField(null=True),
        ),
    ]