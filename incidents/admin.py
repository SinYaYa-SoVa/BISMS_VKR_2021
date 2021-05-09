from django.contrib import admin

# Register your models here.

from .models import Incident
from .models import Employee
from .models import Department
from .models import GRIIB

admin.site.register(Incident)
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(GRIIB)