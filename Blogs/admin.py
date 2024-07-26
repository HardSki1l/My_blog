from django.contrib import admin
from .models import TaskList, UserModelBlog


class TaskSearch(admin.ModelAdmin):
    search_fields = ['who__username']

    def save_model(self, request, obj, form, change):
        obj.name = obj.comment
        obj.save()


class UserSearch(admin.ModelAdmin):
    search_fields = ['username']

    def save_model(self, request, obj, form, change):
        obj.name = obj.username
        obj.save()


admin.site.register(TaskList, TaskSearch)
admin.site.register(UserModelBlog, UserSearch)

# Register your models here.
