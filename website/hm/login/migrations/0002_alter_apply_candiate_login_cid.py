# Generated by Django 4.1 on 2022-09-22 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0001_initial'),
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply_candiate_login',
            name='cid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruitment.applying_candidate'),
        ),
    ]