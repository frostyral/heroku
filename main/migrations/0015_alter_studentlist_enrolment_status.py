# Generated by Django 4.0.4 on 2022-05-04 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_delete_university'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentlist',
            name='enrolment_status',
            field=models.CharField(choices=[('PENDING', 'PENDING'), ('ADMITTED', 'ADMITTED'), ('REJECTED', 'REJECTED')], default='PENDING', max_length=10, verbose_name='Enrolment Status'),
        ),
    ]
