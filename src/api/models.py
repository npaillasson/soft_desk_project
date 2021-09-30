from django.conf import settings
from django.db import models


class Projects(models.Model):

    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=240)
    description = models.CharField(max_length=1000)
    type = models.CharField(max_length=120)


class Contributors(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project_id = models.ForeignKey(to=Projects, on_delete=models.CASCADE)
    permission = models.BooleanField()
    body = models.CharField(max_length=8192, blank=True)
    role = models.CharField(max_length=120)


class Issues(models.Model):
    project_id = models.ForeignKey(to=Projects, on_delete=models.CASCADE)
    title = models.CharField(max_length=240)
    description = models.CharField(max_length=1000)
    tag = models.CharField(max_length=120)
    status = models.CharField(max_length=120)
    priority = models.CharField(max_length=120)
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='auther_user')
    assignee_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='assignee_user')
    created_time = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    issue_id = models.ForeignKey(to=Issues, on_delete=models.CASCADE)
    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    created_time = models.DateTimeField(auto_now_add=True)