from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import NotFound
from .models import Comment, Contributor, Issue, Project


def get_project(project_id):
    try:
        project = Project.objects.get(id=project_id)
    except ObjectDoesNotExist:
        raise NotFound()
    return project


def get_contributor(project_id, user_id):
    try:
        contributor = Contributor.objects.get(project_id=project_id, user_id=user_id)
    except ObjectDoesNotExist:
        raise NotFound()
    return contributor


def get_issue(id):
    try:
        issue = Issue.objects.get(id=id)
    except ObjectDoesNotExist:
        raise NotFound()
    return issue


def get_comment(id):
    try:
        comment = Comment.objects.get(id=id)
    except ObjectDoesNotExist:
        raise NotFound()
    return comment
