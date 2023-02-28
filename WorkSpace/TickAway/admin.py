from django.contrib import admin
from .models import Post

# Register your models here.

class PostAdmin (admin.ModelAdmin):

	list_display = ("season_episode","title", "icon", "description", "date_added","time")

admin.site.register (Post, PostAdmin)
