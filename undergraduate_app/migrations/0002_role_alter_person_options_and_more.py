# Generated by Django 4.1 on 2022-09-11 07:44

from django.db import migrations, models
import utilities.customized_id


class Migration(migrations.Migration):

    dependencies = [
        ('undergraduate_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.CharField(default=utilities.customized_id.create_id, editable=False, max_length=36, primary_key=True, serialize=False)),
                ('value', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['last_name']},
        ),
        migrations.RenameField(
            model_name='person',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='person',
            name='last_name',
            field=models.CharField(default='noone', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='professor',
            name='rolls',
            field=models.ManyToManyField(to='undergraduate_app.role'),
        ),
    ]