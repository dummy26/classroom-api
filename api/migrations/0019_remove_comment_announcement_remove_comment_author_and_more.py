# Generated by Django 4.0.2 on 2022-04-27 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_submission_points'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='announcement',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
        migrations.DeleteModel(
            name='Announcement',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
