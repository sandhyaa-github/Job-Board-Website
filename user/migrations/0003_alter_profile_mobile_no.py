# Generated by Django 3.2.6 on 2023-10-13 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_profile_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='mobile_no',
            field=models.BigIntegerField(blank=True, db_index=True, null=True),
        ),
    ]
