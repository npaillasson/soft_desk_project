from django.urls import path
from .views import ProjectList, ProjectDetails, ProjectUsers

urlpatterns = [
    path("projects/", ProjectList.as_view(), name="Projects_list"),
    path("projects/<int:project_id>/", ProjectDetails.as_view(), name="Projects_list"),
    path(
        "projects/<int:project_id>/users/", ProjectUsers.as_view(), name="project_users"
    ),
    #    path("projects/<int:project_id>/users/<int:user_id>),
]
