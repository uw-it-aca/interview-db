# Copyright 2023 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.test import TestCase
from django.urls import reverse
from interview_db.models import *


class LoginRedirect(TestCase):
    def setUp(self):
        joe = Student.objects.create(
            first_name="Joe",
            last_name="Average",
            follow_up_consent=False,
        )
        interview = Interview.objects.create(
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
        self.interview = interview

    def test_redirect_home(self):
        """
        Test upon loading home page redirects to SAML login page
        """
        url = reverse("interview_db:home")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], "/saml/login?next=/")

    def test_redirect_interview(self):
        """
        Test navigating to student inteview page redirects to SAML login page
        """
        url = reverse("interview_db:student-detail",
                      kwargs={"id": self.interview.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"],
                         "/saml/login?next=/api/students/1/")
