from django.contrib import admin
from .models import Create_notes
# Register your models here.
@admin.register(Create_notes)
class CreatenotesAdmin(admin.ModelAdmin):
    list_display=['note','contact','created_date']
