# Generated by Django 2.0.2 on 2018-02-06 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drone',
            old_name='manufactguring_date',
            new_name='manufacturing_date',
        ),
    ]
