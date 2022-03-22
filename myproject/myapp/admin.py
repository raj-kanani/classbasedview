from django.contrib import admin

# Register your models here.
from .models import Todos

@admin.register(Todos)
class TodosAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'details', 'date']