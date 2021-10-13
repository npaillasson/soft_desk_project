from rest_framework import serializers
from accounts.models import User
from rest_framework.relations import StringRelatedField, SlugRelatedField
from .models import Project, Contributor, Issue, Comment


class ChoiceField(serializers.ChoiceField):
    def to_representation(self, obj):
        return self._choices[int(obj)]


class ProjectSerializer(serializers.ModelSerializer):

    author_username = serializers.SerializerMethodField()
    type = ChoiceField(Project.TYPE_CHOICES)

    def get_author_username(self, obj):
        print(self)
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
    permission = serializers.BooleanField(required=True)

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
    author_user = serializers.SerializerMethodField()
    assignee_user = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="username"
    )
    status = ChoiceField(choices=Issue.STATUS_CHOICES)
    priority = ChoiceField(choices=Issue.PRIORITY_CHOICES)

    def get_author_user(self, obj):
        return str(obj.author_user)

    def get_assignee_user(self, obj):
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
            "author_user",
            "assignee_user_id",
            "assignee_user",
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
    author_username = serializers.SerializerMethodField()
    type = ChoiceField(choices=Project.TYPE_CHOICES)

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


class ContributorDetailsSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="username"
    )
    user_first_name = serializers.SerializerMethodField()
    user_last_name = serializers.SerializerMethodField()
    user_email = serializers.SerializerMethodField()
    project_id = serializers.SlugRelatedField(read_only=True, slug_field="id")
    permission = serializers.BooleanField(required=True)

    def get_user_object(self):
        return User.objects.get(id=self.instance.user_id)

    def get_user_first_name(self, obj):
        return self.get_user_object().first_name

    def get_user_last_name(self, obj):
        return self.get_user_object().last_name

    def get_user_email(self, obj):
        return self.get_user_object().email

    class Meta:
        model = Contributor
        fields = [
            "user_id",
            "user",
            "user_first_name",
            "user_last_name",
            "user_email",
            "project_id",
            "permission",
            "role",
        ]


class IssueDetailsSerializer(serializers.ModelSerializer):
    project_id = serializers.SlugRelatedField(read_only=True, slug_field="id")
    author_user = serializers.SerializerMethodField()
    assignee_user = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="username"
    )
    status = ChoiceField(choices=Issue.STATUS_CHOICES)
    priority = ChoiceField(choices=Issue.PRIORITY_CHOICES)

    def get_author_user(self, obj):
        return str(obj.author_user)

    def get_assignee_user(self, obj):
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
            "author_user",
            "assignee_user_id",
            "assignee_user",
            "created_time",
        ]
