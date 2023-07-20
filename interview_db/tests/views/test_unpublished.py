# Copyright 2023 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.test import TestCase
from django.urls import reverse
from interview_db.models import *
import json


class UnpublishedInterviewsTest(TestCase):
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
            pull_quote="Some pull quote",
            other_publishing_restrictions=False
        )
        self.no_release = no_release

        stu = Student.objects.create(
            first_name="Stu",
            follow_up_consent=True,
        )
        needs_follow_up = Interview.objects.create(
            student=stu,
            date="2021-09-29",
            signed_release_form=False,
            image_is_not_identifying=True,
            intended_major=True,
            no_identifying_photo=True,
            no_real_name=False,
            no_publishing_stories=False,
            pull_quote="Some pull quote",
            other_publishing_restrictions=False
        )
        self.needs_follow_up = needs_follow_up

        publishable = Interview.objects.create(
            student=joe,
            date="2021-09-29",
            signed_release_form=True,
            image_is_not_identifying=True,
            intended_major=True,
            no_identifying_photo=True,
            no_real_name=False,
            no_publishing_stories=False,
            pull_quote="Some pull quote",
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

    def test_release_form(self):
        """
        Tests an interview without a signed release form is not published
        """
        url = reverse("interview_db:student-list")
        response = self.client.get(url, follow=True)
        interviews = json.loads(response.content)
        self.assertEquals(response.status_code, 200)
        self.assertTrue(self.no_release.id not in interviews)

    def test_follow_up_consent(self):
        """
        Tests an interview needing follow up consent is not published
        """
        url = reverse("interview_db:student-list")
        response = self.client.get(url, follow=True)
        interviews = json.loads(response.content)
        self.assertEquals(response.status_code, 200)
        self.assertTrue(self.needs_follow_up.id not in interviews)

    def test_no_pull_quote(self):
        """
        Tests an interview without a pull quote is not published
        """
        url = reverse("interview_db:student-list")
        response = self.client.get(url, follow=True)
        interviews = json.loads(response.content)
        self.assertEquals(response.status_code, 200)
        self.assertTrue(self.no_quote.id not in interviews)
