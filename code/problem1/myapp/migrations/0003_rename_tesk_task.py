# Generated by Django 4.2.1 on 2023-05-20 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_tesk_delete_person'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tesk',
            new_name='Task',
        ),
    ]