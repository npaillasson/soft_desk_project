from rest_framework import mixins, generics
from rest_framework.permissions import IsAuthenticated
from .models import Comments, Contributors, Issues, Projects
from .serializer import CommentsSerializer, ContributorsSerializer, IssuesSerializer, ProjectsSerializer


class ProjectList(generics.ListCreateAPIView):
    permission_classes = ([IsAuthenticated])
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
