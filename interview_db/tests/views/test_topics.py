# Copyright 2023 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.test import TestCase
from django.urls import reverse
from interview_db.models import *
import json


class CollectionsTest(TestCase):
    fixtures = ["interview.json"]

    def setUp(self):
        # creates test interview
        joe = Student.objects.create(
            first_name="Joe",
            follow_up_consent=False,
        )

        i_joe = Interview.objects.create(
            student=joe,
            date="2021-09-29",
            signed_release_form=True,
            image_is_not_identifying=True,
            intended_major=True,
            no_identifying_photo=True,
            no_real_name=False,
            no_publishing_stories=False,
            other_publishing_restrictions=False
        )

        s_joe = Story.objects.create(
            interview=i_joe,
            story_order_position=1,
        )
        c_joe = Coding(
            code=Code.objects.get_or_create(code="Lifelong Learning")[0],
            story=s_joe,
        )
        c_joe.subcode = SubCode.objects.get_or_create(subcode="Context")[0]
        c_joe.save()

        s_joe_2 = Story.objects.create(
            interview=i_joe,
            story_order_position=2,
        )
        c_joe_2 = Coding(
            code=Code.objects.get_or_create(code="Finding Community")[0],
            story=s_joe_2,
        )
        c_joe_2.subcode = SubCode.objects.get_or_create(subcode="Context")[0]
        c_joe_2.save()

        self.i_joe = i_joe

    def tearDown(self):
        Coding.objects.all().delete()
        Story.objects.all().delete()
        Code.objects.all().delete()
        SubCode.objects.all().delete()
        Collection.objects.all().delete()
        Interview.objects.all().delete()
        Student.objects.all().delete()

    def test_interview_topics(self):
        """
        Test the collections returned for this interview
        """
        url = reverse("interview_db:interview-topics", kwargs={
            "id": self.i_joe.id})
        response = self.client.get(url, follow=True)
        topics = json.loads(response.content)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(topics), 2)
        self.assertEquals(topics[0]['topic'], "Finding Community")
        self.assertEquals(topics[1]['topic'], "Self Reflection")

    def test_story_topics(self):
        """
        Test the student detail view, where each story is associated
        with its corresponding topic
        """
        url = reverse("interview_db:student-detail", kwargs={
            "id": self.i_joe.id})
        response = self.client.get(url, follow=True)
        stories = json.loads(response.content)
        topic_1 = stories[0]['collections']
        self.assertEquals(topic_1[0]['topic'], "Self Reflection")
        topic_2 = stories[1]['collections']
        self.assertEquals(topic_2[0]['topic'], "Finding Community")
        self.assertEquals(response.status_code, 200)
