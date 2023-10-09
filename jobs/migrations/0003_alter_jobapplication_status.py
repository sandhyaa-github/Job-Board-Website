# Generated by Django 3.2.6 on 2023-10-09 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_alter_joblisting_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='status',
            field=models.CharField(choices=[('applied', 'viewed_by_recruiter'), ('shortlisted', 'not shortlisted'), ('awaiting for response', 'selected')], max_length=100),
        ),
    ]