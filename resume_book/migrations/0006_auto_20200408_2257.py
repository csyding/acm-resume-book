# Generated by Django 2.2.5 on 2020-04-08 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume_book', '0005_student_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='resumeID',
        ),
        migrations.AddField(
            model_name='student',
            name='courseWork',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='experiences',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='gradYear',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='projects',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.DeleteModel(
            name='Resume',
        ),
    ]
