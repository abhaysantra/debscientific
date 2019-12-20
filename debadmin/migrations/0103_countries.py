# Generated by Django 2.2.6 on 2019-12-09 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debadmin', '0102_delete_country'),
    ]

    operations = [
        migrations.CreateModel(
            name='countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_id', models.IntegerField(null=True)),
                ('sortname', models.CharField(max_length=255, null=True)),
                ('name', models.CharField(max_length=250, null=True)),
                ('phonecode', models.IntegerField(null=True)),
            ],
        ),
    ]
