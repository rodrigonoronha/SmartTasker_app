# Generated by Django 5.1.1 on 2024-09-10 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['created_at']},
        ),
    ]
