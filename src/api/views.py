from rest_framework import mixins, generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
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


class ProjectUsers(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ContributorSerializer
    lookup_url_kwarg = "project_id"

    def get_queryset(self):
        return Contributor.objects.filter(project_id=self.kwargs["project_id"])

    def perform_create(self, serializer):
        project = Project.objects.get(id=self.kwargs["project_id"])
        serializer.save(project_id=project)

    def destroy(self, request, *args, **kwargs):
        instance = Contributor.objects.filter(
            project_id=self.kwargs["project_id"], id=self.kwargs["pk"]
        )
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProjectIssues(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = IssueSerializer
    lookup_url_kwarg = "project_id"

    def perform_create(self, serializer):
        project = Project.objects.get(self.kwargs["project_id"])

        serializer.save(
            project_id=project,
        )

    def get_queryset(self):
        return Issue.objects.filter(project_id=self.kwargs["project_id"])


class ProjectComments(viewsets.ModelViewSet):
    pass
