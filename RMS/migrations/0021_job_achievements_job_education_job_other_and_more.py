# Generated by Django 4.2.5 on 2024-01-30 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RMS', '0020_company_phone_company_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='achievements',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='education',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='other',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='profileprofessional',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='softskills',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='technicalskills',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='workexperience',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
