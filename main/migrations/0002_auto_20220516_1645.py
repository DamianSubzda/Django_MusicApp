# Generated by Django 2.1.5 on 2022-05-16 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='Time',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, max_length=20),
        ),
    ]