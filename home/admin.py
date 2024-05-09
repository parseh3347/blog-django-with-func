from django.contrib import admin
from .models import Todo
# Register your models here.

@admin.register(Todo)

class TodoPostAdmin(admin.ModelAdmin):
    list_display=[
        'title',
        'body',
        'created',
        'update',
        'publish',
    ]
    list_filter=['title', 'created', 'publish']
    search_fields = ['title', 'created', 'publish']
    date_hierarchy = 'created'  
    # list_select_related = ['title']
