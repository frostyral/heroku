# Generated by Django 4.0.4 on 2022-05-13 18:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_studentlist_contact_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentlist',
            name='contact_number',
            field=models.PositiveBigIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(9000000000)], verbose_name='Contact Number (+63)'),
        ),
        migrations.AlterField(
            model_name='studentlist',
            name='steward_contact_number',
            field=models.PositiveBigIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(9000000000)], verbose_name='Contact Number (+63)'),
        ),
    ]
