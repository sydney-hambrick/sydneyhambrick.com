# Generated by Django 4.1.3 on 2022-11-14 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_name', models.CharField(help_text='Enter name of job', max_length=200)),
                ('business_name', models.CharField(help_text='Enter name of business', max_length=200)),
                ('year_worked', models.CharField(help_text='Enter dates worked', max_length=200)),
                ('job_description', models.CharField(help_text='Enter job duties', max_length=1000)),
            ],
            options={
                'ordering': ['-year_worked'],
            },
        ),
    ]