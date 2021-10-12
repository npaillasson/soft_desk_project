from rest_framework import permissions
from .models import Project


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        #  return
        return True


class IsContributor(permissions.BasePermission):
    def has_permission(self, request, view):
        print(request.user.__dict__)
        project = Project.objects.get(id=request.parser_context["kwargs"]["project_id"])
        contributors_list = project.contributors.all()
        for contributor in contributors_list:
            if contributor.user == request.user:
                return True
        return False
