# Generated by Django 3.2.2 on 2022-08-02 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_auto_20220802_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='book',
            name='hora',
        ),
        migrations.RemoveField(
            model_name='book',
            name='lugar',
        ),
    ]
