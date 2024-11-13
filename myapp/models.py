from django.db import models
# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)       # 姓名字段
    age = models.IntegerField()                   # 年龄字段
    email = models.EmailField()                   # 邮箱字段

    def __str__(self):
        return self.name
