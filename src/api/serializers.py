from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.relations import StringRelatedField, SlugRelatedField
from .models import Project, Contributor, Issue, Comment


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "author_user_id",
            "title",
            "description",
            "type",
        ]


class ContributorSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="username"
    )
    project_id = serializers.SlugRelatedField(read_only=True, slug_field="id")

    class Meta:
        model = Contributor
        fields = [
            "id",
            "user_id",
            "user",
            "project_id",
            "permission",
            "role",
        ]


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = [
            "id",
            "project_id",
            "title",
            "description",
            "tag",
            "status",
            "priority",
            "author_user_id",
            "assignee_user_id",
            "created_time",
        ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "id",
            "issue_id",
            "author_user_id",
            "description",
            "created_time",
        ]


class ProjectDetailsSerializer(serializers.ModelSerializer):
    contributors = ContributorSerializer(many=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "author_user_id",
            "title",
            "description",
            "type",
            "contributors",
        ]
