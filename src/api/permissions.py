from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    pass


class IsContributor(permissions.BasePermission):
    def has_permission(self, request, view):
        print("héhé", request.__dict__)
        print("haha", view.__dict__)
        return True
