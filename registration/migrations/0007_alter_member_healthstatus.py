# Generated by Django 4.1.7 on 2023-03-23 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_member_todaydate_alter_member_registrationdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='Healthstatus',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='registration.healthstatus'),
        ),
    ]
