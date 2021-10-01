from rest_framework import mixins, generics
from rest_framework.permissions import IsAuthenticated
from .models import Comments, Contributors, Issues, Projects
from .serializers import CommentsSerializer, ContributorsSerializer, IssuesSerializer, ProjectsSerializer


class ProjectList(generics.ListCreateAPIView):
    permission_classes = ([IsAuthenticated])
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer


class ProjectDetails(generics.GenericAPIView, mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    permission_classes = ([IsAuthenticated])
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ProjectUsers(generics.ListCreateAPIView):
    pass
