# Generated by Django 3.2.19 on 2023-05-28 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uaa', '0002_auto_20230523_2345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branch',
            name='phoneNumber',
        ),
        migrations.AddField(
            model_name='branch',
            name='branchEmail',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='email address'),
        ),
    ]
