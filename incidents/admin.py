from django.contrib import admin

# Register your models here.

from .models import Incident
from .models import Employee
from .models import Department
from .models import Info_assets
from .models import Info_objects
from .models import GRIIB

admin.site.register(Incident)
admin.site.register(Employee)
admin.site.register(Department)
# admin.site.register(Info_assets)
# admin.site.register(Info_objects)
admin.site.register(GRIIB)