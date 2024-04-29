# Copyright 2024 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from rest_framework import serializers
from .models import *


class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = ['full_title']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name',
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
    image = serializers.ImageField(max_length=None, use_url=True,
                                   allow_empty_file=True, required=False)
    standing = serializers.CharField(source='get_standing_display')

    class Meta:
        model = Interview
        fields = ['id',
                  'student',
                  'major',
                  'date',
                  'signed_release_form',
                  'pull_quote',
                  'declared_major',
                  'image',
                  'image_is_not_identifying',
                  'image_alt_text',
                  'standing',
                  'no_identifying_photo',
                  'no_real_name',
                  'no_publishing_stories',
                  'other_publishing_restrictions']


class InterviewIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = ['id']


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


class StoryTopicSerializer(serializers.ModelSerializer):
    interview = InterviewSerializer(read_only=True)
    code = CodeSerializer(many=True, read_only=True)
    subcode = SubCodeSerializer(many=True, read_only=True)
    collections = serializers.SerializerMethodField()

    def get_collections(self, Story):
        collections = set()
        for code in Story.code.all():
            for c in Collection.objects.all():
                if code in c.codes.all() or code in c.subcodes.all():
                    collections.add(c)
        for code in Story.subcode.all():
            for c in Collection.objects.all():
                if code in c.codes.all() or code in c.subcodes.all():
                    collections.add(c)
        serializer = CollectionFilterSerializer(collections, many=True)
        return serializer.data

    class Meta:
        model = Story
        fields = ['id',
                  'interview',
                  'code',
                  'subcode',
                  'story',
                  'story_order_position',
                  'collections']


class CollectionSerializer(serializers.ModelSerializer):
    codes = CodeSerializer(read_only=True, many=True)
    subcodes = SubCodeSerializer(read_only=True, many=True)
    # interviews = serializers.SerializerMethodField()

    # def get_interviews(self, Story):
    #     interviews = set()
    #     for code in self.codes:
    #         for story in code.story_set.all():
    #             interviews.add(story.interview)
    #     for subcode in self.subcodes:
    #         for story in subcode.story_set.all():
    #             interviews.add(story.interview)
    #     serializer = InterviewSerializer(interviews, many=True)
    #     return serializer.data

    class Meta:
        model = Collection
        fields = ['id',
                  'topic',
                  'slug',
                  'codes',
                  'subcodes',
                  'question']


class CollectionFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id',
                  'topic',
                  'slug']
