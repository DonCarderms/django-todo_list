from django.contrib import admin

from Todo_List.models import Todo

# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'completed')
admin.site.register(Todo, TodoAdmin)