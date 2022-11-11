from django.db import models


class Order(models.Model):
    department = models.ForeignKey('Department', on_delete=models.CASCADE, null=True, blank=True)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    date_created = models.DateField()
    Телефонная_связь = models.BooleanField(default=False)
    Электронная_почта = models.BooleanField(default=False)
    image = models.ImageField(upload_to='static/dostup2app/img', verbose_name='file', null=True, blank=True)

    class Meta:
        db_table = 'orders'
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ('employee', 'date_created')




class Employee(models.Model):
    management = models.ForeignKey('Management', on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey('Department', on_delete=models.CASCADE, null=True, blank=True)
    name_ru = models.CharField(max_length=200)


    def __str__(self):
        return f"{self.name_ru}"

    class Meta:
        db_table = 'employee'
        verbose_name = 'ФИО сотрудника'
        verbose_name_plural = 'ФИО сотрудников'
        ordering = ('name_ru', )


class Department(models.Model):
    management = models.ForeignKey('Management', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'department'
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'
        ordering = ('name', )


class Management(models.Model):
    name = models.CharField(max_length=200)
    parent = models.ForeignKey(
        'Management',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )


    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = 'management'
        verbose_name = 'Управление'
        verbose_name_plural = 'Управления'
        ordering = ('name', 'id')

# Create your models here.
from django.db import models

# Create your models here.
