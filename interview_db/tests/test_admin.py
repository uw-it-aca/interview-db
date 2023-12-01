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
    session = {'samlUserdata': {'isMemberOf': 'u_test_admin'}}


class AdminTest(TestCase):
    fixtures = ["collections.json"]

    def setUp(self):
        self.user = User.objects.create_user(
            username="javerage", password="pass")
        self.request = MockRequest()
        self.request.user = self.user
        self.site = AdminSite()

        self.student = Student.objects.create(
            first_name="Joe",
            last_name="Average",
            follow_up_consent=False,
        )

        self.interview = Interview.objects.create(
            student=self.student,
            date="2021-09-29",
            signed_release_form=True,
            image_is_not_identifying=True,
            intended_major=True,
            no_identifying_photo=True,
            no_real_name=False,
            no_publishing_stories=False,
            other_publishing_restrictions=False
        )

        self.story = Story.objects.create(
            interview=self.interview,
            story="This is Joe's first story about Learning!",
            story_order_position=1,
        )

        self.major_admin = MajorAdmin(Major, self.site)
        self.student_admin = StudentAdmin(Student, self.site)
        self.interview_admin = InterviewAdmin(Interview, self.site)
        self.coding_admin = CodingAdmin(Coding, self.site)
        self.subcode_admin = SubCodeAdmin(SubCode, self.site)
        self.code_admin = CodeAdmin(Code, self.site)
        self.story_admin = StoryAdmin(Story, self.site)
        self.collection_admin = CollectionAdmin(Collection, self.site)

    def test_redirect(self):
        """
        Test navigating to admin redirects to SAML login page
        """
        url = reverse("admin:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"],
                         "/admin/login/?next=/admin/")

    def test_interview_followup(self):
        self.assertEqual(self.interview_admin.get_followup(self.interview),
                         False)

    def test_story_methods(self):
        self.assertEqual(self.story_admin.get_first_name(self.story),
                         "Joe")
        self.assertEqual(self.story_admin.get_last_name(self.story),
                         "Average")
        self.assertEqual(self.story_admin.get_date(self.story),
                         "2021-09-29")

    def test_permissions_major(self):
        self.assertEqual(self.major_admin.has_view_permission(self.request),
                         False)
        self.assertEqual(self.major_admin.has_add_permission(self.request),
                         False)
        self.assertEqual(self.major_admin.has_change_permission(self.request),
                         False)
        self.assertEqual(self.major_admin.has_delete_permission(self.request),
                         False)
        self.assertEqual(self.major_admin.has_module_permission(self.request),
                         False)

    def test_permissions_student(self):
        self.assertEqual(self.student_admin.has_view_permission(
            self.request), True)
        self.assertEqual(self.student_admin.has_add_permission(
            self.request), True)
        self.assertEqual(self.student_admin.has_change_permission(
            self.request), True)
        self.assertEqual(self.student_admin.has_delete_permission(
            self.request), True)
        self.assertEqual(self.student_admin.has_module_permission(
            self.request), True)

    def test_permissions_interview(self):
        self.assertEqual(self.interview_admin.has_view_permission(
            self.request), True)
        self.assertEqual(self.interview_admin.has_add_permission(
            self.request), True)
        self.assertEqual(self.interview_admin.has_change_permission(
            self.request), True)
        self.assertEqual(self.interview_admin.has_delete_permission(
            self.request), True)
        self.assertEqual(self.interview_admin.has_module_permission(
            self.request), True)

    def test_permissions_coding(self):
        self.assertEqual(self.coding_admin.has_view_permission(
            self.request), False)
        self.assertEqual(self.coding_admin.has_add_permission(
            self.request), False)
        self.assertEqual(self.coding_admin.has_change_permission(
            self.request), False)
        self.assertEqual(self.coding_admin.has_delete_permission(
            self.request), False)
        self.assertEqual(self.coding_admin.has_module_permission(
            self.request), False)

    def test_permissions_subcode(self):
        self.assertEqual(self.subcode_admin.has_view_permission(
            self.request), False)
        self.assertEqual(self.subcode_admin.has_add_permission(
            self.request), False)
        self.assertEqual(self.subcode_admin.has_change_permission(
            self.request), False)
        self.assertEqual(self.subcode_admin.has_delete_permission(
            self.request), False)
        self.assertEqual(self.subcode_admin.has_module_permission(
            self.request), False)

    def test_permissions_code(self):
        self.assertEqual(self.code_admin.has_view_permission(
            self.request), False)
        self.assertEqual(self.code_admin.has_add_permission(
            self.request), False)
        self.assertEqual(self.code_admin.has_change_permission(
            self.request), False)
        self.assertEqual(self.code_admin.has_delete_permission(
            self.request), False)
        self.assertEqual(self.code_admin.has_module_permission(
            self.request), False)

    def test_permissions_story(self):
        self.assertEqual(self.story_admin.has_view_permission(
            self.request), True)
        self.assertEqual(self.story_admin.has_add_permission(
            self.request), True)
        self.assertEqual(self.story_admin.has_change_permission(
            self.request), True)
        self.assertEqual(self.story_admin.has_delete_permission(
            self.request), True)
        self.assertEqual(self.story_admin.has_module_permission(
            self.request), True)

    def test_permission_collection(self):
        self.assertEqual(self.collection_admin.has_view_permission(
            self.request), True)
        self.assertEqual(self.collection_admin.has_add_permission(
            self.request), True)
        self.assertEqual(self.collection_admin.has_change_permission(
            self.request), True)
        self.assertEqual(self.collection_admin.has_delete_permission(
            self.request), True)
        self.assertEqual(self.collection_admin.has_module_permission(
            self.request), True)
