# Generated by Django 4.0.4 on 2022-04-27 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_alter_sale_total_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='postions',
            new_name='positions',
        ),
    ]