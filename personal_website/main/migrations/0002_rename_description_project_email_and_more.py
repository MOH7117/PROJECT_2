# Generated by Django 4.1.6 on 2023-02-10 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='description',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='rating',
            new_name='phone',
        ),
    ]