# Generated by Django 3.2.1 on 2021-05-07 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Department_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Time', models.TimeField()),
                ('Source', models.CharField(choices=[('EMP', 'Работник организации БС РФ'), ('TCH', 'Техническое средство')], max_length=3)),
                ('Describtion', models.TextField()),
                ('Violation_fact', models.CharField(default='Нет', max_length=255)),
                ('Violator_info', models.CharField(default='Нет', max_length=255)),
                ('Tech_Fault_Fact', models.CharField(choices=[('DEAD', 'Выход из строя СЗИ'), ('FALT', 'Сбой СЗИ'), ('INAC', 'Недоступность критичной для выполнения функций СЗИ информации'), ('INTG', 'Нарушение целостности программного обеспечения СЗИ'), ('PARM', 'Отклонение параметров настроек СЗИ'), ('MALF', 'Снижение функциональных характеристик (параметров) СЗИ')], default='Нет', max_length=255)),
                ('Violation_Realisation_fact', models.CharField(default='Нет', max_length=4)),
                ('ISR_violation_fact', models.CharField(choices=[('CONF', 'Конфиденциальность'), ('INTG', 'Целостность'), ('ACCS', 'Доступность'), ('OTHR', 'Иные свойства')], default='Нет', max_length=4)),
                ('unauth_behavior', models.CharField(choices=[('VIOL', 'Нарушение установленного порядка и режима дня'), ('OFFS', 'Отклонение от сложившегося порядка и режима использования информационных ресурсов')], default='Нет', max_length=4)),
                ('premed_fact', models.CharField(choices=[('RAND', 'Случайный'), ('INTD', 'Намеренный'), ('MIST', 'Ошибочный')], max_length=4)),
                ('level_detection', models.CharField(choices=[('COMM', 'Обычная'), ('HIGH', 'Высокая')], max_length=4)),
                ('information_asset', models.CharField(choices=[('ACCD', 'Cвершившийся'), ('ATMP', 'Попытка осуществления инцидента ИБ'), ('SUSP', 'Подозрение на инцидент ИБ')], max_length=4)),
                ('incident_type_OLEG1', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIO', models.CharField(max_length=255, verbose_name='ФИО')),
                ('Position', models.CharField(max_length=255, verbose_name='Должность')),
                ('Role', models.CharField(choices=[('User', 'Пользователь'), ('AABS', 'Администратор АБС'), ('AIS', 'Администратор ИБ'), ('EIS', 'Работник службы ИБ')], max_length=4, verbose_name='Роль')),
                ('Contacts', models.CharField(max_length=12, verbose_name='Номер телефона')),
                ('Department', models.ManyToManyField(to='incidents.Department')),
            ],
        ),
    ]
