from django.conf import settings
from django.db import models


class Project(models.Model):

    author_user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="author_username",
    )
    title = models.CharField(max_length=240)
    description = models.CharField(max_length=1000)
    type = models.CharField(max_length=120)


class Contributor(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project_id = models.ForeignKey(
        to=Project, on_delete=models.CASCADE, related_name="contributors"
    )
    permission = models.BooleanField()
    role = models.CharField(max_length=120)

    def __str__(self):
        return str(self.user)


class Issue(models.Model):
    PRIORITY_CHOICES = [(4, "Critique"), (3, "Fort"), (2, "Moyen"), (1, "Faible")]
    STATUS_CHOICES = [(1, "En cours"), (2, "En test"), (3, "Validé")]
    project_id = models.ForeignKey(
        to=Project, on_delete=models.CASCADE, related_name="issues"
    )
    title = models.CharField(max_length=240)
    description = models.CharField(max_length=1000)
    tag = models.CharField(max_length=120)
    status = models.CharField(choices=STATUS_CHOICES, max_length=1)
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=1)
    author_user_id = models.ForeignKey(
        to=Contributor,
        on_delete=models.CASCADE,
        related_name="author_user",
    )
    assignee_user_id = models.ForeignKey(
        to=Contributor,
        on_delete=models.CASCADE,
        related_name="assignee_user",
    )
    created_time = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    issue_id = models.ForeignKey(to=Issue, on_delete=models.CASCADE)
    author_user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    description = models.CharField(max_length=1000)
    created_time = models.DateTimeField(auto_now_add=True)
