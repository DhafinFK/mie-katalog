# Generated by Django 4.2.4 on 2023-09-12 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indomie',
            name='type',
            field=models.CharField(choices=[('MG', 'Mie Goreng'), ('MK', 'Mie Kuah')], max_length=2),
        ),
    ]
