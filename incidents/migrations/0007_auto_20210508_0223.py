# Generated by Django 3.2.1 on 2021-05-07 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incidents', '0006_auto_20210508_0220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tech_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='incident',
            name='Emp',
            field=models.ManyToManyField(blank=True, to='incidents.Employee'),
        ),
        migrations.RemoveField(
            model_name='incident',
            name='Tch',
        ),
        migrations.AddField(
            model_name='incident',
            name='Tch',
            field=models.ManyToManyField(blank=True, to='incidents.Tech'),
        ),
    ]