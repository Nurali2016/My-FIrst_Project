# Generated by Django 4.1.5 on 2023-03-06 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_dostavka_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='dostavka',
            name='all_price',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
