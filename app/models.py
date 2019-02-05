from django.contrib import admin
from django.db import models

# Create your models here.


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    cat_name = models.CharField(max_length=15)

    def __str__(self):
        return self.cat_name


class CategoryAdmin(admin.ModelAdmin):
    pass


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created = models.DateField(auto_now=True)
    post_name = models.CharField(max_length=200)
    post_body = models.CharField(max_length=2000)

    def __str__(self):
        return self.post_name


class PostAdmin(admin.ModelAdmin):
    search_fields = ['post_name']
    date_hierarchy = 'created'
    list_filter = ('category', 'post_name')
