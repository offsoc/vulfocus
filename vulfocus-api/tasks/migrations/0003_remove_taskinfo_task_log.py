# Generated by Django 2.2.10 on 2020-05-28 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_taskinfo_task_log'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskinfo',
            name='task_log',
        ),
    ]