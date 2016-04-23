from django.contrib import admin
from .models import RecurringTask, DeadlineTask, RecurringEvent, RecurringComment, DeadlineComment, Notes


class RecurringTaskAdmin(admin.ModelAdmin):
    list_display        =       ['task_name','description','frequency']
    list_display_links  =       ['task_name','description','frequency']
    list_filter         =       ['task_name','description','frequency']
    search_fields       =       ['task_name','description','frequency']

    class Meta:
        model = RecurringTask

class RecurringEventAdmin(admin.ModelAdmin):
    list_display        =       ['task','started_time','completed_time']

    class Meta:
        model = RecurringEvent

class RecurringCommentAdmin(admin.ModelAdmin):
    list_display        =       ['event','comment']

    class Meta:
        model = RecurringComment

class DeadlineTaskAdmin(admin.ModelAdmin):
    list_display        =       ['task_name','description']

    class Meta:
        model = DeadlineTask

class DeadlineCommentAdmin(admin.ModelAdmin):
    list_display        =       ['task','comment']

    class Meta:
        model = DeadlineComment


class NotesAdmin(admin.ModelAdmin):
    list_display        =       ['title']

admin.site.register(RecurringTask, RecurringTaskAdmin)
admin.site.register(RecurringEvent, RecurringEventAdmin)
admin.site.register(RecurringComment, RecurringCommentAdmin)
admin.site.register(DeadlineTask, DeadlineTaskAdmin)
admin.site.register(DeadlineComment, DeadlineCommentAdmin)
admin.site.register(Notes,NotesAdmin)

# Register your models here.
