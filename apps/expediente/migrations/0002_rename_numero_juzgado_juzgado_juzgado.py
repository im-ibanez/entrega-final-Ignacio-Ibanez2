# Generated by Django 4.2.1 on 2023-05-27 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expediente', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='juzgado',
            old_name='numero_juzgado',
            new_name='juzgado',
        ),
    ]