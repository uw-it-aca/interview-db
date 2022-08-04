from rest_framework import serializers
from .models import *


class StudentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentType
        fields = ['type']


class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = ['full_title', 'major_abbreviation']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'uw_netid']


class InterviewSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    major = MajorSerializer(many=True, read_only=True)

    class Meta:
        model = Interview
        fields = ['date',
                  'signed_release_form',
                  'pull_quote',
                  'image',
                  'image_is_not_identifying',
                  'intended_major',
                  'standing',
                  'years_until_graduation',
                  'current_year',
                  'no_identifying_photo',
                  'no_real_name',
                  'no_publishing_stories',
                  'other_publishing_restrictions']


class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = ['topic', 'code', 'definition']


class StorySerializer(serializers.ModelSerializer):
    interview = InterviewSerializer(read_only=True)
    code = CodeSerializer(many=True, read_only=True)

    class Meta:
        model = Story
        fields = ['story', 'story_order_position']


class CodingSerializer(serializers.ModelSerializer):
    code = CodeSerializer(read_only=True)
    story = StorySerializer(read_only=True)

    class Meta:
        model = Coding
