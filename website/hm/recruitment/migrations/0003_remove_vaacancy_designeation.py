# Generated by Django 4.1 on 2022-09-26 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0002_alter_vaacancy_dept_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vaacancy',
            name='designeation',
        ),
    ]
