# Generated by Django 2.2.6 on 2019-11-07 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debadmin', '0066_review_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(null=True),
        ),
    ]
