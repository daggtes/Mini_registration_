# Generated by Django 4.1.7 on 2023-03-23 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0011_alter_member_dateofbirth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='Age',
        ),
        migrations.AlterField(
            model_name='member',
            name='CreatedBy',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='Gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='UpdatedBy',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
