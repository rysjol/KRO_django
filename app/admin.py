from django.contrib import admin
from .models import Category, CategoryAdmin
from .models import Post, PostAdmin

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

