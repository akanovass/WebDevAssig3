from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Post, Category, Author  # Пример нескольких моделей

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Author)
