from django.urls import path
from .views import ProjectList, ProjectDetails, ProjectUsers

urlpatterns = [
    path("projects/", ProjectList.as_view(), name="Projects_list"),
    path("projects/<int:pk>/", ProjectDetails.as_view(), name="Projects_list"),
    path("projects/<int:pk>/users/", ProjectUsers.as_view(), name="project_users"),
]
