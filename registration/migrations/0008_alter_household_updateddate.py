# Generated by Django 4.1.7 on 2023-03-23 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_alter_member_healthstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='household',
            name='UpdatedDate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
