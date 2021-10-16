from rest_framework import permissions
from rest_framework.exceptions import NotFound
from rest_framework.permissions import SAFE_METHODS
from .functions import get_contributor, get_project


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS or request.method == "POST":
            return True
        return request.user == obj.author_user


class IsContributor(permissions.BasePermission):
    def has_permission(self, request, view):
        project = get_project(project_id=request.parser_context["kwargs"]["project_id"])
        contributors_list = project.contributors.all()
        for contributor in contributors_list:
            if contributor.user == request.user:
                return True
        raise NotFound()


class CanAddContributors(permissions.BasePermission):
    def has_permission(self, request, view):
        project = get_project(project_id=request.parser_context["kwargs"]["project_id"])
        contributor_user = request.user.contributor_set.get(
            project_id=request.parser_context["kwargs"]["project_id"], user=request.user
        )
        if request.method in SAFE_METHODS:
            return True
        elif request.method == "DELETE":
            obj = get_contributor(
                project_id=request.parser_context["kwargs"]["project_id"],
                user_id=request.parser_context["kwargs"]["pk"],
            )
            return self.has_object_permission(
                request, view, obj, project, contributor_user
            )
        elif project.author_user == contributor_user:
            return True
        return request.user.contributor_set.get(
            project_id=request.parser_context["kwargs"]["project_id"]
        ).permission

    def has_object_permission(self, request, view, obj, project, contributor_user):
        if project.author_user_id == obj.user_id:
            return False
        elif contributor_user.user_id == obj.user_id:
            return True
        elif project.author_user_id == contributor_user.user_id:
            return True
        elif contributor_user.permission and not obj.permission:
            return True
        return False
