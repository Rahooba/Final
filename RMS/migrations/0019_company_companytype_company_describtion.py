# Generated by Django 4.2.5 on 2024-01-29 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RMS', '0018_alter_applicant_email_alter_company_about_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='companytype',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='describtion',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
