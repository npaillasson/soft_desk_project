from rest_framework import serializers
from .models import Projects, Contributors, Issues, Comments


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id','author_user_id', 'author_user_id', 'title', 'description', 'type', ]


class ContributorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributors
        fields = ['id', 'user', 'project_id', 'permission', 'body', 'role', ]


class IssuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issues
        fields = ['id', 'project_id', 'title', 'description', 'tag', 'status', 'priority',
                  'author_user_id', 'assignee_user_id', 'created_time', ]


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'issue_id', 'author_user_id', 'description', 'created_time', ]
