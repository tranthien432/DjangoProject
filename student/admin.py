from django.contrib import admin
from .models import Students, ClassST


class StudentAdmin(admin.ModelAdmin):
    list_display = ('nameST', 'birthday', 'gender', 'email', 'state', 'class_id')


class ClassAdmin(admin.ModelAdmin):
    list_display = ('classname', 'classtype')


admin.site.register(Students, StudentAdmin)
admin.site.register(ClassST, ClassAdmin)
