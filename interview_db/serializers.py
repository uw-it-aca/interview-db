# Copyright 2023 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from rest_framework import serializers
from .models import *


class StudentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentType
        fields = ['id', 'type']


class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = ['id', 'full_title', 'major_abbreviation']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'email', 'uw_netid',
                  'follow_up_consent']


class SubCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCode
        fields = ['id', 'subcode', 'definition']


class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = ['id', 'topic', 'code', 'definition']


class InterviewSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    major = MajorSerializer(many=True, read_only=True)
    # major = major_display
    student_type = StudentTypeSerializer(many=True, read_only=True)
    image_url = serializers.ImageField(max_length=None, use_url=True,
                                       allow_null=True, required=False)
    standing = serializers.CharField(source='get_standing_display')

    class Meta:
        model = Interview
        fields = ['id',
                  'student',
                  'major',
                  'date',
                  'interview_quarter',
                  'signed_release_form',
                  'pull_quote',
                  'declared_major',
                  'image',
                  'image_url',
                  'image_is_not_identifying',
                  'image_alt_text',
                  'intended_major',
                  'standing',
                  'years_until_graduation',
                  'current_year',
                  'student_type',
                  'no_identifying_photo',
                  'no_real_name',
                  'no_publishing_stories',
                  'other_publishing_restrictions']


class StorySerializer(serializers.ModelSerializer):
    interview = InterviewSerializer(read_only=True)
    code = CodeSerializer(many=True, read_only=True)
    subcode = SubCodeSerializer(many=True, read_only=True)

    class Meta:
        model = Story
        fields = ['id',
                  'interview',
                  'code',
                  'subcode',
                  'story',
                  'story_order_position']


class CodingSerializer(serializers.ModelSerializer):
    code = CodeSerializer(read_only=True)
    subcode = SubCodeSerializer(read_only=True)
    story = StorySerializer(read_only=True)

    class Meta:
        model = Coding
        fields = ['id',
                  'code',
                  'subcode',
                  'story']


class CollectionSerializer(serializers.ModelSerializer):
    codes = CodeSerializer(read_only=True, many=True)
    subcodes = SubCodeSerializer(read_only=True, many=True)

    class Meta:
        model = Collection
        fields = ['id',
                  'topic',
                  'slug',
                  'codes',
                  'subcodes',
                  'question']
