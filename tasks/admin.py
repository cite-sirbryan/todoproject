from django.contrib import admin

# Register your models here.
from .models import *


# interface of the admin (personal preference)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "complete", "created")
    list_editable = ("title", "complete")

class PersonAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "address", "birthday")
    list_editable = ("name", "address", "birthday")


admin.site.register(Task, TaskAdmin)
admin.site.register(Person, PersonAdmin)
