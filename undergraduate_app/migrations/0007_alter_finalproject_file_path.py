# Generated by Django 4.1.3 on 2022-11-23 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('undergraduate_app', '0006_remove_departmenthead_rolls_remove_professor_rolls_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalproject',
            name='file_path',
            field=models.TextField(),
        ),
    ]