# Generated by Django 4.1.5 on 2023-02-22 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_dostavka_delete_mymodilim'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dostavka',
            options={'ordering': ['id'], 'verbose_name': 'Dastavka', 'verbose_name_plural': 'Dastavka'},
        ),
    ]
