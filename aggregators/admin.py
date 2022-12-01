from django.contrib import admin
from .models import Article, Channel

# Register your models here.

@admin.register(Article)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("series_name", "name", "topic", "created_time",)

admin.site.register(Channel)
