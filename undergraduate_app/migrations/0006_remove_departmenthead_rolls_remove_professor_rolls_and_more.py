# Generated by Django 4.1.3 on 2022-11-21 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('undergraduate_app', '0005_alter_status_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departmenthead',
            name='rolls',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='rolls',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]