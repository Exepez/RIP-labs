# Generated by Django 3.1.4 on 2021-01-14 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0022_auto_20210114_1324'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.AlterModelOptions(
            name='motherboard',
            options={'verbose_name': 'Материнская плата', 'verbose_name_plural': 'Материнские платы'},
        ),
        migrations.DeleteModel(
            name='ReviewCPU',
        ),
    ]
