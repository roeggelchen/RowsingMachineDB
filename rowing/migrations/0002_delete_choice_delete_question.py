# Generated by Django 4.0.1 on 2022-01-14 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rowing', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
