# Generated by Django 4.1.7 on 2023-03-23 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0009_beneficiarytype_alter_member_educationlevel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='Age',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]