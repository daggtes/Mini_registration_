# Generated by Django 4.1.7 on 2023-03-24 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0016_remove_member_createdby'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='UpdatedBy',
        ),
    ]
