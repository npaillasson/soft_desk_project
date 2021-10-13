from django.urls import path
from rest_framework import routers
from .views import ProjectList, ProjectDetails, ProjectUsers, ProjectIssues


urlpatterns = [
    path("projects/", ProjectList.as_view(), name="Projects_list"),
    path("projects/<int:project_id>/", ProjectDetails.as_view(), name="Projects_list"),
    path(
        "projects/<int:project_id>/users/",
        ProjectUsers.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="project_users",
    ),
    path(
        "projects/<int:project_id>/users/<int:pk>/",
        ProjectUsers.as_view(
            {
                "get": "retrieve",
                "delete": "destroy",
            }
        ),
        name="delete_project_users",
    ),
    path(
        "projects/<int:project_id>/issues/",
        ProjectIssues.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
    ),
    path(
        "projects/<int:project_id>/issues/<int:pk>/comments/",
        ProjectIssues.as_view(
            {
                "put": "update",
            }
        ),
    ),
]
