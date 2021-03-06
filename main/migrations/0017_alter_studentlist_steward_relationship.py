# Generated by Django 4.0.4 on 2022-05-04 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_studentlist_uni_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentlist',
            name='steward_relationship',
            field=models.CharField(choices=[('Father', 'Father'), ('Mother', 'Mother'), ('Brother', 'Brother'), ('Sister', 'Sister'), ('Grandfather', 'Grandfather'), ('Grandmother', 'Grandmother'), ('Foster Parent', 'Foster Parent'), ('Step-Parent', 'Step-Parent'), ('Step-Sibling', 'Step-Sibling'), ('Guardian', 'Guardian')], max_length=20, verbose_name='Relationship'),
        ),
    ]
