# Generated by Django 4.1.6 on 2023-02-10 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024)),
                ('description', models.TextField()),
                ('rating', models.TextField()),
            ],
        ),
    ]
