from django.contrib import admin
from .models import Employee, Position


# Register your models here.
class PositionAdmin(admin.ModelAdmin):
    pass


class EmployeeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Position, PositionAdmin)
admin.site.register(Employee, EmployeeAdmin)
