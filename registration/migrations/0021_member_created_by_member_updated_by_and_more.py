# Generated by Django 4.1.7 on 2023-04-06 16:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('registration', '0020_alter_householdprogram_householdprogram'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='Created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='member',
            name='Updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='household',
            name='Status',
            field=models.IntegerField(choices=[(1, 'Active'), (0, 'Inactive')], default=1, null=True),
        ),
    ]
