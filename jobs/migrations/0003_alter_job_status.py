# Generated by Django 4.0.4 on 2022-05-27 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_rename_jobs_job_rename_references_reference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('IP', 'In progress'), ('WA', 'Waiting for Approval'), ('F', 'Finished')], default='IP', max_length=2),
        ),
    ]
