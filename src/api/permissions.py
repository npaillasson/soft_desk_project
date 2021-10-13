from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS
from .models import Project


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            print("OBJ", obj.__dict__)
            return True
        print(obj.__dict__)
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
