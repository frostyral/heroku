# Generated by Django 4.0.4 on 2022-05-04 10:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_studentlist_enrolment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentlist',
            name='uni_address',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='University Address'),
        ),
        migrations.AlterField(
            model_name='studentlist',
            name='uni_city',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='studentlist',
            name='uni_college',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Previous College'),
        ),
        migrations.AlterField(
            model_name='studentlist',
            name='uni_country',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='studentlist',
            name='uni_course',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Previous Program'),
        ),
        migrations.AlterField(
            model_name='studentlist',
            name='uni_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='studentlist',
            name='uni_reason',
            field=models.TextField(blank=True, null=True, verbose_name='Reason of Transfer'),
        ),
        migrations.AlterField(
            model_name='studentlist',
            name='uni_year',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)], verbose_name='Previous Year'),
        ),
    ]
