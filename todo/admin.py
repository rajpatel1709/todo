from django.contrib import admin
from .models import Task
class TaskAdmin(admin.ModelAdmin) :
    list_display = ( 'task' , 'is_compeleted' , 'updated_at')
    #it must be a tuppple
    search_fields = ('task',)
#inherit classupper here
# Register your models here.
admin.site.register(Task , TaskAdmin)