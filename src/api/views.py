from rest_framework import mixins, generics
from rest_framework.permissions import IsAuthenticated
from .models import Comment, Contributor, Issue, Project
from .serializers import (
    CommentSerializer,
    ContributorSerializer,
    IssueSerializer,
    ProjectSerializer,
    ProjectDetailsSerializer,
)


class ProjectList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        serializer.save(author_user_id=self.request.user)
        Contributor.objects.create(
            user=self.request.user,
            project_id=serializer.instance,
            permission=True,
            role="administrateur projet",
        )


class ProjectDetails(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectDetailsSerializer
    lookup_url_kwarg = "project_id"

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ProjectUsers(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ContributorSerializer
    lookup_url_kwarg = ["project_id", "user_id"]

    def get_queryset(self):
        project = self.kwargs["project_id"]
        print(self.__dict__)
        print(self.lookup_field)
        return Contributor.objects.filter(project_id=project)

    def perform_create(self, serializer):
        project = self.kwargs["project_id"]
        project = Project.objects.get(id=project)
        serializer.save(project_id=project)
