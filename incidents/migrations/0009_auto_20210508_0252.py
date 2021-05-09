# Generated by Django 3.2.1 on 2021-05-07 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0008_auto_20210508_0229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='griib',
            name='Specialists_FIO',
        ),
        migrations.AddField(
            model_name='griib',
            name='Specialists_FIO',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='GRIIBs', to='incidents.employee'),
        ),
        migrations.RemoveField(
            model_name='incident',
            name='Scpec_assigment',
        ),
        migrations.AddField(
            model_name='incident',
            name='Scpec_assigment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Incidents', to='incidents.griib'),
        ),
    ]