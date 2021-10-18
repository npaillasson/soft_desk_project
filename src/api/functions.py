from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import NotFound
from accounts.models import User
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


def get_contributor_by_username(project_id, username):
    user = User.objects.get(username=username)
    get_contributor(project_id=project_id, user_id=user.id)


def get_issue(project_id, id):
    try:
        issue = Issue.objects.get(project_id=project_id, id=id)
    except ObjectDoesNotExist:
        raise NotFound()
    return issue


def get_comment(issue_id, id):
    try:
        comment = Comment.objects.get(issue_id=issue_id, id=id)
    except ObjectDoesNotExist:
        raise NotFound()
    return comment
