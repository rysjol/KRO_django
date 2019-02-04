from django.db import models

# Create your models here.


class Category(models.Model):
    def __str__(self):
        return self.cat_name
    cat_name = models.CharField(max_length = 15)


class Post(models.Model):
    def __str__(self):
        return self.post_name
    category = models.ForeignKey(Category, on_delete = models.PROTECT)
    created = models.DateField(auto_now = True)
    post_name = models.CharField(max_length=200)
    post_body = models.CharField(max_length=2000)
