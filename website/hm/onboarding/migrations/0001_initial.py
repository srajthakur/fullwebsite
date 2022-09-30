# Generated by Django 4.1 on 2022-09-13 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='creating_employee',
            fields=[
                ('cid', models.IntegerField(default=0, unique=True)),
                ('eid', models.IntegerField(primary_key=True, serialize=False)),
                ('dept_id', models.IntegerField(unique=True)),
                ('bankdetail', models.ImageField(upload_to='images/')),
                ('passport', models.ImageField(upload_to='images/')),
                ('pancard', models.ImageField(upload_to='images/')),
                ('aadharcard', models.ImageField(upload_to='images/')),
                ('status', models.CharField(default='-', max_length=50)),
                ('name', models.CharField(default='-', max_length=50)),
                ('designeation', models.CharField(default='-', max_length=50)),
                ('contact', models.CharField(default='-', max_length=50)),
                ('age', models.CharField(default='-', max_length=50)),
                ('mail', models.EmailField(default='-', max_length=50)),
                ('gender', models.CharField(default='-', max_length=50)),
            ],
        ),
    ]
