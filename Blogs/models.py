from django.db import models



class UserModelBlog(models.Model):
    objects = None
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=16)

    def __str__(self):
        return self.username


class TaskList(models.Model):
    objects = None
    date = models.DateTimeField(auto_now_add=True)  # hozirgi vaqtni oladigan funksiya auto now add true
    comment = models.TextField(max_length=255)
    who = models.ManyToManyField(UserModelBlog)


    def __str__(self):
        return self.comment
