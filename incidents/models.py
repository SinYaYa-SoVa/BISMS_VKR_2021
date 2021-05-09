from django.db import models


# Create your models here.




class Department(models.Model):
   Department_name = models.CharField(max_length=255)
   def __str__(self):
      return self.Department_name



class Employee(models.Model):
   Roles = (
      ('User', 'Пользователь'),
      ('AABS', 'Администратор АБС'),
      ('AIS', 'Администратор ИБ'),
      ('EIS', 'Работник службы ИБ')
   )
   FIO = models.CharField('ФИО', max_length=255)
   Department = models.ForeignKey("Department", related_name='Employees', null=True,  on_delete=models.SET_NULL)
   Position = models.CharField('Должность', max_length=255)
   Role = models.CharField('Роль', max_length=4, choices=Roles)
   Contacts = models.CharField('Номер телефона', max_length=12)

   def __str__(self):
      return self.FIO

class Tech(models.Model):
   Tech_name = models.CharField(max_length=255)
   def __str__(self):
      return self.Tech_name

class GRIIB(models.Model):
   Specialists_FIO = models.ForeignKey("Employee", related_name='GRIIBs', null=True,  on_delete=models.SET_NULL)


class Info_assets(models.Model):
   Asset_name = models.CharField(max_length=255)
   def __str__(self):
      return self.Asset_name

class Info_objects(models.Model):
   Object_name = models.CharField(max_length=255)
   def __str__(self):
      return self.Object_name


class Incident(models.Model):
   Date = models.DateField()
   Time = models.TimeField()

   Sources = (
      ("EMP", "Работник организации БС РФ"),
      ("TCH", "Техническое средство")
   )
   Source = models.CharField(max_length=3, choices=Sources)
   Emp = models.ManyToManyField(Employee, blank=True)
   Tch = models.ManyToManyField(Tech, blank=True)
   Describtion = models.TextField()
   Violation_fact = models.CharField(max_length=255, default="Нет")
   Violator_info = models.CharField(max_length=255, default="Нет")
   Tech_Fault_Facts = (
      ('DEAD', 'Выход из строя СЗИ'),
      ('FALT', 'Сбой СЗИ'),
      ('INAC', 'Недоступность критичной для выполнения функций СЗИ информации'),
      ('INTG', 'Нарушение целостности программного обеспечения СЗИ'),
      ('PARM', 'Отклонение параметров настроек СЗИ'),
      ('MALF', 'Снижение функциональных характеристик (параметров) СЗИ')
   )
   Tech_Fault_Fact = models.CharField(max_length=255, default="Нет", choices=Tech_Fault_Facts)
   Violation_Realisation_fact = models.CharField(max_length=4, default="Нет")
   ISR_violation_facts = (
      ('CONF', 'Конфиденциальность'),
      ('INTG', 'Целостность'),
      ('ACCS', 'Доступность'),
      ('OTHR', 'Иные свойства')
   )
   ISR_violation_fact = models.CharField(max_length=4, default="Нет", choices=ISR_violation_facts )
   unauth_behaviors = (
      ('VIOL', 'Нарушение установленного порядка и режима дня'),
      ('OFFS', 'Отклонение от сложившегося порядка и режима использования информационных ресурсов')
   )
   Unauth_behavior = models.CharField(max_length=4, default="Нет", choices=unauth_behaviors)
   premed_facts = (
      ('RAND', 'Случайный'),
      ('INTD', 'Намеренный'),
      ('MIST', 'Ошибочный')
   )
   Premed_fact = models.CharField(max_length=4, choices=premed_facts)
   incident_type = (
      ('ACCD', 'Cвершившийся'),
      ('ATMP', 'Попытка осуществления инцидента ИБ'),
      ('SUSP', 'Подозрение на инцидент ИБ')
   )
   Level_detection = models.CharField(max_length=4, choices=(('COMM', 'Обычная'), ('HIGH', 'Высокая')))

   Information_asset = models.ManyToManyField(Info_assets)
   Information_object = models.ManyToManyField(Info_objects)

   banksprocc = (
      ('PAYT', 'Платежные технологические процессы'),
      ('INFO', 'Информационные технологические процессы')
   )
   BankTechProcc = models.CharField(max_length=4, default='Нет', choices=banksprocc)

   levels_incident = (
      ('PHIS', 'Физический'),
      ('NETW', 'Сетевой'),
      ('OS', 'Операционных систем'),
      ('BD', 'Систем управления базами данных'),
      ('BTEC', 'Банковских технологических процессов и приложений'),
      ('BPRC', 'Бизнес-процессов организации')
   )
   Level_incident = models.CharField(max_length=4, choices=levels_incident)

   Consequences_level = (
      ('MIN', 'Минимальный'),
      ('MAX', 'Средняя'),
      ('MID', 'Высокая'),
      ('CRIT', 'Критическая')
   )
   Consequences = models.CharField(max_length=4, default='Нет', choices=Consequences_level)
   Recurrence_possibility = models.CharField(max_length=4, default='Нет', choices=Consequences_level)
   range_list = (
      ('MIN', 'Пределы одной АБС'),
      ('MAX', 'Пределы отдельного структурного подразделения организации БС РФ'),
      ('MID', 'Организации БС РФ в целом'),
      ('CRIT', 'Выходящий за пределы организации БС РФ')
   )
   Range = models.CharField(max_length=4, choices=range_list)
   priority_list = (
      ('0', 'Наивысший'),
      ('1', 'Высокий'),
      ('2', 'Повышенный'),
      ('3', 'Средний'),
      ('4', 'Низкий'),
      ('5', 'Минимальный')
   )
   Incident_priority = models.CharField(max_length=1, choices=priority_list)
   Incident_urgency = models.CharField(max_length=4, choices=(('COMM', 'Обычная'), ('HIGH', 'Высокая')))
   Incident_report = models.CharField(max_length=255, default='Нет')
   Incident_elimination_report = models.CharField(max_length=255, default='Нет')
   Incident_escalation = models.CharField(max_length=3, choices=(('YES', 'Да'), ('NO', 'Нет')))
   Functional_group = models.CharField(max_length=255, default='Нет')
   Functional_group_time = models.CharField(max_length=255, default='Нет')
   Scpec_assigment = models.ForeignKey("GRIIB", related_name='Incidents', null=True,  on_delete=models.SET_NULL)
   incident_statuses = (
      ('REGI', 'Зарегистрирован'),
      ('ASSG', 'Назначен'),
      ('WORK', 'В работе'),
      ('CLSD', 'Закрыт')
   )
   Incident_status = models.CharField(max_length=4, choices=incident_statuses)
   Closed_date = models.DateField(auto_now_add=False)
   Consequences_org = models.TextField(default='Нет')
   Incident_closure_level = models.CharField(max_length=4, choices=(('COMM', 'Обычная'), ('HIGH', 'Высокая')))
   Departments_alerts = models.ManyToManyField(Department, blank=True)