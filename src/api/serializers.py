from rest_framework import serializers
from accounts.models import User
from rest_framework.relations import StringRelatedField, SlugRelatedField
from .models import Project, Contributor, Issue, Comment


class ProjectSerializer(serializers.ModelSerializer):

    author_user_id = serializers.SlugRelatedField(read_only=True, slug_field="id")
    author_username = serializers.SerializerMethodField()

    def get_author_username(self, obj):
        return str(obj.author_user_id)

    class Meta:
        model = Project
        fields = [
            "id",
            "author_user_id",
            "author_username",
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
            "user_id",
            "user",
            "project_id",
            "permission",
            "role",
        ]


class IssueSerializer(serializers.ModelSerializer):
    project_id = serializers.SlugRelatedField(read_only=True, slug_field="id")
    author_username = serializers.SerializerMethodField()
    assignee_username = serializers.SerializerMethodField()

    def get_author_username(self, obj):
        return str(obj.author_user_id)

    def get_assignee_username(self, obj):
        return str(obj.assignee_user_id)

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
            "author_username",
            "assignee_user_id",
            "assignee_username",
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
    issues = IssueSerializer(many=True)
    author_user_id = serializers.SlugRelatedField(read_only=True, slug_field="id")
    author_username = serializers.SerializerMethodField()

    def get_author_username(self, obj):
        return str(obj.author_user_id)

    class Meta:
        model = Project
        fields = [
            "id",
            "author_user_id",
            "author_username",
            "title",
            "description",
            "type",
            "contributors",
            "issues",
        ]
