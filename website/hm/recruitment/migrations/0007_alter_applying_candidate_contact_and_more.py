# Generated by Django 4.1 on 2022-09-28 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0006_remove_applying_candidate_cv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applying_candidate',
            name='contact',
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.AlterField(
            model_name='applying_candidate',
            name='mail',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]