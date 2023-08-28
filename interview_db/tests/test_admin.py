# Copyright 2023 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.test import TestCase
from django.urls import reverse
from interview_db.models import *
from django.contrib.admin.sites import AdminSite
from interview_db.admin import *
from unittest.mock import Mock


class AdminTest(TestCase):
    fixtures = ["collections.json"]

    def setUp(self):
        self.site = AdminSite()

    def test_redirect(self):
        """
        Test navigating to admin redirects to SAML login page
        """
        url = reverse("admin:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"],
                         "/admin/login/?next=/admin/")

    # def test_collection(self):
    #     collections_admin = CollectionAdmin(Collection, self.site)
