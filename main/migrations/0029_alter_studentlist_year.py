# Generated by Django 4.0.4 on 2022-05-28 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_delete_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentlist',
            name='year',
            field=models.CharField(choices=[('1st Year', '1st Year'), ('2nd Year', '2nd Year'), ('3rd Year', '3rd Year'), ('4th Year', '4th Year'), ('5th Year', '5th Year')], max_length=8, verbose_name='Year Level'),
        ),
    ]
