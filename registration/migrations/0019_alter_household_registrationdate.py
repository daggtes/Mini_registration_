# Generated by Django 4.1.7 on 2023-03-24 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0018_alter_household_updateddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='household',
            name='RegistrationDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
