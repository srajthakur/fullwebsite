# Generated by Django 4.1 on 2022-09-13 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('dept_id', models.IntegerField(primary_key=True, serialize=False)),
                ('department_name', models.CharField(default='-', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='designation',
            fields=[
                ('designation_id', models.CharField(default='-', max_length=10, primary_key=True, serialize=False)),
                ('designation_name', models.CharField(default='-', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='emp_detail',
            fields=[
                ('eid', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('name', models.CharField(default='-', max_length=50)),
                ('designation', models.CharField(default='-', max_length=50)),
                ('contact', models.IntegerField(default=0, unique=True)),
                ('age', models.CharField(default='-', max_length=50)),
                ('mail', models.EmailField(max_length=50, unique=True)),
                ('gender', models.CharField(default='-', max_length=50)),
                ('cid', models.IntegerField(default=0, unique=True)),
                ('dept_id', models.IntegerField(default=0, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='pay_slip_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_wd', models.IntegerField(default='-')),
                ('total_present', models.IntegerField(default='-')),
                ('total_absent', models.IntegerField(default='-')),
                ('total_payment', models.IntegerField(default='-')),
                ('eid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employeedetail.emp_detail')),
            ],
        ),
        migrations.CreateModel(
            name='leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_oh', models.IntegerField()),
                ('left_oh', models.IntegerField()),
                ('total_cl', models.IntegerField()),
                ('left_cl', models.IntegerField()),
                ('total_sl', models.IntegerField()),
                ('left_sl', models.IntegerField()),
                ('eid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employeedetail.emp_detail')),
            ],
        ),
        migrations.CreateModel(
            name='emp_salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hra', models.CharField(default='-', max_length=10)),
                ('basic', models.CharField(default='-', max_length=10)),
                ('pfc', models.CharField(default='-', max_length=10)),
                ('pfe', models.CharField(default='-', max_length=10)),
                ('insurance1', models.CharField(default='-', max_length=10)),
                ('insurance2', models.CharField(default='-', max_length=10)),
                ('total', models.CharField(default='-', max_length=10)),
                ('eid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employeedetail.emp_detail')),
            ],
        ),
        migrations.CreateModel(
            name='emp_roll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(default='-', max_length=50)),
                ('designation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employeedetail.designation')),
                ('eid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employeedetail.emp_detail')),
            ],
        ),
        migrations.CreateModel(
            name='emp_document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadharcaed', models.ImageField(upload_to='images/')),
                ('pancard', models.ImageField(upload_to='images/')),
                ('passport', models.ImageField(upload_to='images/')),
                ('bank_detail', models.ImageField(upload_to='images/')),
                ('eid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employeedetail.emp_detail')),
            ],
        ),
        migrations.CreateModel(
            name='attandance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default='-')),
                ('timein', models.TimeField(default='00:00:00')),
                ('timeout', models.TimeField(default='00:00:00')),
                ('remark', models.CharField(default='Absent', max_length=19)),
                ('eid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employeedetail.emp_detail')),
            ],
        ),
    ]
