from django.contrib import admin

# Register your models here.
from .models import * 

# interface of the admin (personal preference)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id','title','complete','created')
    list_editable = ('title', 'complete')


admin.site.register(Task,TaskAdmin)
