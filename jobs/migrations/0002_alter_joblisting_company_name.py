# Generated by Django 3.2.6 on 2023-10-09 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joblisting',
            name='company_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posted_by', to='user.employerprofile'),
        ),
    ]
