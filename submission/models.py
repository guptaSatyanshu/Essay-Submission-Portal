from django.db import models

from student.models import UsersAccount


class StudentEssay(models.Model):
    user = models.ForeignKey(UsersAccount, on_delete=models.CASCADE)
    title = models.CharField(max_length=400)
    body = models.TextField()

    def __str__(self):
        return self.title



