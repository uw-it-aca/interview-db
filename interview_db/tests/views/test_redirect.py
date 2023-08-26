# Copyright 2023 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.test import TestCase
from django.urls import reverse
from interview_db.models import *
import json


class LoginRedirect(TestCase):

    def test_redirect(self):
        """
        Test upon loading home page redirects to SAML login page
        """
        url = reverse("interview_db:home")
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/saml/login?next=/")
