from django.contrib import admin
from .models import Management, Department, Employee, Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('department', 'employee', 'date_created')
    list_filter = ('employee', )
    date_hierarchy = 'date_created'
    fieldsets = (
        ('Основные настройки', {'fields': ('department', 'employee', 'date_created')}),
        ('Доп настройки', {'fields': ('image', 'Телефонная_связь', 'Электронная_почта')})
    )



@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'management', 'department')
    list_filter = ('department', 'name_ru')
    search_fields = ('name_ru', )


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('management', 'name')
    list_filter = ('management', 'name')
    search_fields = ('name',)

@admin.register(Management)
class ManagementAdmin(admin.ModelAdmin):
    empty_value_display = 'H/Y'
    list_display = ('name', 'id')
    list_filter = ('name', )
    search_fields = ('name', )
    search_help_text = 'введите наименование управления'


# Register your models here.
from django.contrib import admin

# Register your models here.
