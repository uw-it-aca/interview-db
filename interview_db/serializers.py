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
        fields = ['full_title']


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
    student_type = StudentTypeSerializer(many=True, read_only=True)
    image = serializers.ImageField(max_length=None, use_url=True,
                                   allow_empty_file=True, required=False)
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


class InterviewCollectionSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    major = MajorSerializer(many=True, read_only=True)
    student_type = StudentTypeSerializer(many=True, read_only=True)
    image = serializers.ImageField(max_length=None, use_url=True,
                                   allow_empty_file=True, required=False)
    standing = serializers.CharField(source='get_standing_display')
    collections = serializers.SerializerMethodField()

    def get_collections(self, Interview):
        interview = Story.objects.filter(interview__id=Interview.id)
        queryset = []
        list = set()
        for s in interview:
            if (s.code.all().count() > 0):
                # print(s.code.all())
                list.add(s.code.all())

            if (s.subcode.all().count() > 0):
                # print(s.subcode.all())
                list.add(s.subcode.all())
        
        for code in list:
            for c in Collection.objects.all():
                if code[0] in c.codes.all() or code[0] in c.subcodes.all():
                    queryset.append(c)

        print("here")
        queryset = [*set(queryset)]
        serializer = CollectionSerializer(queryset, many=True)
        return serializer.data

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
                  'other_publishing_restrictions',
                  'collections']


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
