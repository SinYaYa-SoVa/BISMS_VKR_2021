# Generated by Django 3.2.1 on 2021-05-07 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0007_auto_20210508_0223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='Department',
        ),
        migrations.AddField(
            model_name='employee',
            name='Department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Employees', to='incidents.department'),
        ),
    ]
