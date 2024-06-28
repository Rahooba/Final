# Generated by Django 4.2.5 on 2024-02-01 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RMS', '0031_remove_company_joptitle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicant',
            name='cvl',
        ),
        migrations.RemoveField(
            model_name='applicant',
            name='jobs',
        ),
        migrations.RemoveField(
            model_name='applicant',
            name='skills',
        ),
        migrations.RemoveField(
            model_name='job',
            name='education',
        ),
        migrations.RemoveField(
            model_name='skils',
            name='experienc',
        ),
        migrations.AddField(
            model_name='applicant',
            name='about',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='applicant',
            name='biography',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='applicant',
            name='jobname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='applicant',
            name='location',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='applicant',
            name='volanteering',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='applicant',
            name='workexperience',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='applicants',
            field=models.ManyToManyField(to='RMS.applicant'),
        ),
        migrations.AddField(
            model_name='skils',
            name='applicant',
            field=models.ManyToManyField(to='RMS.applicant'),
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, null=True)),
                ('role', models.CharField(max_length=1000, null=True)),
                ('tools', models.CharField(max_length=1000, null=True)),
                ('describtion', models.CharField(max_length=1000, null=True)),
                ('applicant', models.ManyToManyField(to='RMS.applicant')),
            ],
        ),
    ]
