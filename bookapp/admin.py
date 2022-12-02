from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {'slug': ('name',)}



class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    
admin.site.register(Book, BookAdmin)