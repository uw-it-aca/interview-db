# Copyright 2023 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.test import TestCase
from django.urls import reverse
from interview_db.models import *
import json


class UnpublishedInterviewsTest(TestCase):
    fixtures = ["collections.json"]

    def setUp(self):
        joe = Student.objects.create(
            first_name="Joe",
            follow_up_consent=False,
        )
        no_release = Interview.objects.create(
            student=joe,
            date="2021-09-29",
            signed_release_form=False,
            image_is_not_identifying=True,
            intended_major=True,
            no_identifying_photo=True,
            no_real_name=False,
            no_publishing_stories=False,
            pull_quote="Did not sighn release form",
            other_publishing_restrictions=False
        )
        self.no_release = no_release

        publishable = Interview.objects.create(
            student=joe,
            date="2021-09-29",
            signed_release_form=True,
            image_is_not_identifying=True,
            intended_major=True,
            no_identifying_photo=True,
            no_real_name=False,
            no_publishing_stories=False,
            pull_quote="Able to be published",
            other_publishing_restrictions=False
        )
        self.publishable = publishable

        no_quote = Interview.objects.create(
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
        self.no_quote = no_quote

        story_publishable = Story.objects.create(
            interview=publishable,
            story="This is a publishable story about Getting Help",
            story_order_position=1,
            )
        coding_publishable = Coding(
            code=Code.objects.get_or_create(topic="Career",
                                            code="Getting Help")[0],
            story=story_publishable,
        )
        coding_publishable.subcode = SubCode.objects.get_or_create(
            subcode="Context")[0]
        coding_publishable.save()

        coding_publishable_2 = Coding(
            code=Code.objects.get_or_create(topic="Learning",
                                            code="Lifelong Learning")[0],
            story=story_publishable,
        )
        coding_publishable_2.subcode = SubCode.objects.get_or_create(
            subcode="Context")[0]
        coding_publishable_2.save()
        self.story_publishable = story_publishable

        story_no_release = Story.objects.create(
            interview=no_release,
            story="This is a no-release story about Getting Help",
            story_order_position=1,
            )
        coding_no_release = Coding(
            code=Code.objects.get_or_create(topic="Career",
                                            code="Getting Help")[0],
            story=story_no_release,
        )
        coding_no_release.subcode = SubCode.objects.get_or_create(
            subcode="Context")[0]
        coding_no_release.save()
        self.story_no_release = story_no_release

        story_no_quote = Story.objects.create(
            interview=no_quote,
            story="This is a no-quote story about Working Towards Goals",
            story_order_position=1,
            )
        coding_no_quote = Coding(
            code=Code.objects.get_or_create(code="Lifelong Learning")[0],
            story=story_no_quote,
        )
        coding_no_quote.subcode = SubCode.objects.get_or_create(
            subcode="Context")[0]
        coding_no_quote.save()
        self.story_no_quote = story_no_quote

    def tearDown(self):
        Interview.objects.all().delete()
        Student.objects.all().delete()
        Major.objects.all().delete()

    def test_no_release_form(self):
        """
        Tests an interview without a signed release form is not published
        """
        url = reverse("interview_db:student-list")
        response = self.client.get(url, follow=True)
        interviews = json.loads(response.content)
        self.assertEqual(self.publishable.id, interviews[0]["id"])
        self.assertNotEqual(self.no_release.id, interviews[0]["id"])

        url = reverse("interview_db:random-students")
        response = self.client.get(url, follow=True)
        random = json.loads(response.content)
        self.assertEqual(self.publishable.id, random[0]["id"])
        self.assertNotEqual(self.no_release.id, random[0]["id"])

    def test_no_pull_quote(self):
        """
        Tests an interview without a pull quote is not published
        """
        url = reverse("interview_db:student-list")
        response = self.client.get(url, follow=True)
        interviews = json.loads(response.content)
        self.assertEqual(self.publishable.id, interviews[0]["id"])
        self.assertNotEqual(self.no_release.id, interviews[0]["id"])

        url = reverse("interview_db:random-students")
        response = self.client.get(url, follow=True)
        random = json.loads(response.content)
        self.assertEqual(self.publishable.id, random[0]["id"])
        self.assertNotEqual(self.no_release.id, random[0]["id"])

    def test_invalid_pull_quote(self):
        """
        Tests an interview with an invalid pull quote is not published
        """
        self.no_quote.pull_quote = ''
        url = reverse("interview_db:student-list")
        response = self.client.get(url, follow=True)
        interviews = json.loads(response.content)
        self.assertEqual(self.publishable.id, interviews[0]["id"])
        self.assertNotEqual(self.no_release.id, interviews[0]["id"])

        url = reverse("interview_db:random-students")
        response = self.client.get(url, follow=True)
        random = json.loads(response.content)
        self.assertEqual(self.publishable.id, random[0]["id"])
        self.assertNotEqual(self.no_release.id, random[0]["id"])

    def test_collection_no_release(self):
        """
        Tests a collection will not return stories from interviews without
        a signed release form
        """
        topic_id = Collection.objects.get(topic="Getting Help").id
        url = reverse("interview_db:collection-stories",  kwargs={
            "id": topic_id})
        response = self.client.get(url, follow=True)
        stories = json.loads(response.content)
        self.assertEqual(len(stories), 1)
        self.assertEqual(self.story_publishable.id, stories[0]["id"])
        self.assertNotEqual(self.story_no_release.id, stories[0]["id"])

    def test_collection_no_quote(self):
        """
        Tests a collection will not return stories from interviews without
        a valid pull quote
        """
        topic_id = Collection.objects.get(topic="Self Reflection").id
        url = reverse("interview_db:collection-stories",  kwargs={
            "id": topic_id})
        response = self.client.get(url, follow=True)
        stories = json.loads(response.content)
        self.assertEqual(len(stories), 1)
        self.assertEqual(self.story_publishable.id, stories[0]["id"])
        self.assertNotEqual(self.story_no_quote.id, stories[0]["id"])

    def test_interview_count(self):
        """
        Tests interview count returns a count of only publishable interviews
        """
        url = reverse("interview_db:interview-count")
        response = self.client.get(url, follow=True)
        count = json.loads(response.content)
        self.assertEqual(count, 1)

    def tearDown(self):
        pass
