# Generated by Django 4.0.2 on 2022-04-17 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_resume_education_resume_work_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Jtitle', models.CharField(max_length=100)),
                ('cname', models.CharField(max_length=100)),
                ('Jquali', models.CharField(max_length=100)),
                ('Jloacation', models.CharField(max_length=100)),
                ('Jsalary', models.PositiveBigIntegerField()),
            ],
        ),
    ]
