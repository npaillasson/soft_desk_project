from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Comments, Contributors, Issues, Projects
from .serializer import CommentsSerializer, ContributorsSerializer, IssuesSerializer, ProjectsSerializer

@csrf_exempt
def project_list(request):

    if request.method == 'GET':
        projetcs = Projects.objects.all()
        serializer = ProjectsSerializer(projetcs, many=True)
        return JsonResponse(serializer.data, safe=False)
