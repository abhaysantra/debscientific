# Generated by Django 2.2.6 on 2019-11-07 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debadmin', '0064_product_avg_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(null=True)),
                ('product_id', models.IntegerField(null=True)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('message', models.TextField(null=True)),
                ('date', models.DateField(null=True)),
            ],
        ),
    ]
