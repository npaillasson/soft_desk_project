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


class ProjectDetails(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectDetailsSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# class ProjectUsers(generics.ListCreateAPIView):
#    permission_classes = ([IsAuthenticated])
#    queryset = Projects.objects.all()
#    serializer_class =
