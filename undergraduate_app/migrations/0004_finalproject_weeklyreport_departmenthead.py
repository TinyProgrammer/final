# Generated by Django 4.1.3 on 2022-11-21 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('undergraduate_app', '0003_report_status_request_report_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinalProject',
            fields=[
                ('report_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='undergraduate_app.report')),
                ('accepted', models.BooleanField()),
                ('file_path', models.FilePathField()),
            ],
            bases=('undergraduate_app.report',),
        ),
        migrations.CreateModel(
            name='WeeklyReport',
            fields=[
                ('report_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='undergraduate_app.report')),
            ],
            bases=('undergraduate_app.report',),
        ),
        migrations.CreateModel(
            name='DepartmentHead',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='undergraduate_app.person')),
                ('rolls', models.ManyToManyField(to='undergraduate_app.role')),
                ('specialized_fields', models.ManyToManyField(to='undergraduate_app.field')),
            ],
            bases=('undergraduate_app.person',),
        ),
    ]
