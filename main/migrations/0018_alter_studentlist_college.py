# Generated by Django 4.0.4 on 2022-05-04 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_studentlist_steward_relationship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentlist',
            name='college',
            field=models.CharField(max_length=30),
        ),
    ]
