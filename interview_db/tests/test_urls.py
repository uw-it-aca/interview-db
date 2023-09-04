# Copyright 2023 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.test import TestCase
from django.urls import resolve
from interview_db.models import *


class UrlTest(TestCase):
    def test_home_url(self):
        resolver = resolve('/')
        self.assertEqual('interview_db:home', resolver.view_name)

    def test_view_home_url(self):
        response = self.client.get('/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_admin_url(self):
        resolver = resolve('/admin')
        self.assertEqual('interview_db:admin:index', resolver.view_name)

    def test_view_admin_url(self):
        response = self.client.get('/admin/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_students_url(self):
        resolver = resolve('/students')
        self.assertEqual('interview_db:students', resolver.view_name)

    def test_view_students_url(self):
        response = self.client.get('/students/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_collections_url(self):
        resolver = resolve('/collections')
        self.assertEqual('interview_db:collections', resolver.view_name)

    def test_view_collections_url(self):
        response = self.client.get('/collections/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_about_url(self):
        resolver = resolve('/about')
        self.assertEqual('interview_db:about', resolver.view_name)

    def test_view_about_url(self):
        response = self.client.get('/about/', follow=True)
        self.assertEqual(response.status_code, 200)
