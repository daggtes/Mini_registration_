# Generated by Django 4.1.7 on 2023-03-23 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0013_alter_household_femalemembersize_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='UpdatedDate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
