# Copyright 2023 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from interview_db.models import *
from django.contrib.admin.sites import AdminSite
from interview_db.admin import *
import mock
from django.contrib.sessions.middleware import SessionMiddleware

admin_group = settings.INTERVIEW_DB_AUTHZ_GROUPS['admin']


class MockRequest:
    pass


class AdminTest(TestCase):
    fixtures = ["collections.json"]

    def setUp(self):
        self.user = User.objects.create_user(
            username="javerage", password="pass")
        self.site = AdminSite()
        self.collection = Collection.objects.create(
            topic="Moving Forward")
        self.collection.code = Code.objects.get_or_create(
            code="Finding Community")[0]
        self.collection.subcode = SubCode.objects.get_or_create(
            subcode="Context")[0]
        self.collection.save()

    def test_redirect(self):
        """
        Test navigating to admin redirects to SAML login page
        """
        url = reverse("admin:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"],
                         "/admin/login/?next=/admin/")

    def test_permissions_major(self):
        admin = MajorAdmin(Major, self.site)
        request = MockRequest()
        request.user = self.user
        self.assertEqual(admin.has_view_permission(request), False)
        self.assertEqual(admin.has_add_permission(request), False)
        self.assertEqual(admin.has_change_permission(request), False)
        self.assertEqual(admin.has_delete_permission(request), False)
        self.assertEqual(admin.has_module_permission(request), False)

    def test_permissions_student(self):
        admin = StudentAdmin(Student, self.site)
        request = MockRequest()
        request.session = {'samlUserdata': {'isMemberOf': 'u_test_admin'}}
        request.user = self.user
        self.assertEqual(admin.has_view_permission(request), True)
        self.assertEqual(admin.has_add_permission(request), True)
        self.assertEqual(admin.has_change_permission(request), True)
        self.assertEqual(admin.has_delete_permission(request), True)
        self.assertEqual(admin.has_module_permission(request), True)

    def test_permissions_interview(self):
        admin = InterviewAdmin(Interview, self.site)
        request = MockRequest()
        request.session = {'samlUserdata': {'isMemberOf': 'u_test_admin'}}
        request.user = self.user
        self.assertEqual(admin.has_view_permission(request), True)
        self.assertEqual(admin.has_add_permission(request), True)
        self.assertEqual(admin.has_change_permission(request), True)
        self.assertEqual(admin.has_delete_permission(request), True)
        self.assertEqual(admin.has_module_permission(request), True)

    def test_permissions_coding(self):
        admin = CodingAdmin(Coding, self.site)
        request = MockRequest()
        request.user = self.user
        self.assertEqual(admin.has_view_permission(request), False)
        self.assertEqual(admin.has_add_permission(request), False)
        self.assertEqual(admin.has_change_permission(request), False)
        self.assertEqual(admin.has_delete_permission(request), False)
        self.assertEqual(admin.has_module_permission(request), False)

    def test_permissions_subcode(self):
        admin = SubCodeAdmin(SubCode, self.site)
        request = MockRequest()
        request.user = self.user
        self.assertEqual(admin.has_view_permission(request), False)
        self.assertEqual(admin.has_add_permission(request), False)
        self.assertEqual(admin.has_change_permission(request), False)
        self.assertEqual(admin.has_delete_permission(request), False)
        self.assertEqual(admin.has_module_permission(request), False)

    def test_permissions_code(self):
        admin = CodeAdmin(Code, self.site)
        request = MockRequest()
        request.user = self.user
        self.assertEqual(admin.has_view_permission(request), False)
        self.assertEqual(admin.has_add_permission(request), False)
        self.assertEqual(admin.has_change_permission(request), False)
        self.assertEqual(admin.has_delete_permission(request), False)
        self.assertEqual(admin.has_module_permission(request), False)

    def test_permissions_story(self):
        admin = StoryAdmin(Story, self.site)
        request = MockRequest()
        request.session = {'samlUserdata': {'isMemberOf': 'u_test_admin'}}
        request.user = self.user
        self.assertEqual(admin.has_view_permission(request), True)
        self.assertEqual(admin.has_add_permission(request), True)
        self.assertEqual(admin.has_change_permission(request), True)
        self.assertEqual(admin.has_delete_permission(request), True)
        self.assertEqual(admin.has_module_permission(request), True)

    def test_permission_collection(self):
        admin = CollectionAdmin(Collection, self.site)
        request = MockRequest()
        request.user = self.user
        self.assertEqual(admin.has_view_permission(request), False)
        self.assertEqual(admin.has_add_permission(request), False)
        self.assertEqual(admin.has_change_permission(request), False)
        self.assertEqual(admin.has_delete_permission(request), False)
        self.assertEqual(admin.has_module_permission(request),
                         False)
