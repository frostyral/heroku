# Generated by Django 4.0.4 on 2022-05-01 12:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_studentlist_contact_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentlist',
            name='country',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='PreviousUniversity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.studentlist')),
            ],
        ),
        migrations.CreateModel(
            name='ParentGuardian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=10)),
                ('relationship', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('home_address', models.CharField(max_length=50)),
                ('contact_number', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(99999999999), django.core.validators.MinValueValidator(0)])),
                ('email', models.EmailField(max_length=254)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.studentlist')),
            ],
        ),
    ]