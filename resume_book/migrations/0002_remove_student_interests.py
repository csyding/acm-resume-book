# Generated by Django 2.2.11 on 2020-05-04 02:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume_book', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='interests',
        ),
    ]
