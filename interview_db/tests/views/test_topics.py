# Copyright 2023 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.test import TestCase
from django.urls import reverse
from interview_db.models import *
import json


class InterviewTopicsTest(TestCase):
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

        self.i_joe = i_joe

    def test_topics(self):
        """
        Test the collections returned for this interview
        """
        url = reverse("interview_db:interview-topics", kwargs={
            "id": self.i_joe.id})
        response = self.client.get(url, follow=True)
        topics = json.loads(response.content)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(topics), 1)
        self.assertEquals(topics[0]['topic'], "Self Reflection")
        print(response.content)
