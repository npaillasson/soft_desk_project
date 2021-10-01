from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from .models import Comments, Contributors, Issues, Projects
from .serializer import CommentsSerializer, ContributorsSerializer, IssuesSerializer, ProjectsSerializer


class ProjectList(APIView):
    permission_classes = ([IsAuthenticated])

    def get(self, request, format=None):
        projetcs = Projects.objects.all()
        serializer = ProjectsSerializer(projetcs, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
        serializer = ProjectsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
