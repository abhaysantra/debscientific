# Generated by Django 2.2.6 on 2019-12-09 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debadmin', '0105_states_auto_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_id', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('state_id', models.IntegerField(null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='states',
            old_name='auto_id',
            new_name='state_id',
        ),
    ]
