# Copyright 2022 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0


from django.test import TestCase
from interview_db.models import Student


class StudentModelTest(TestCase):
    def test_str(self):
        student = Student(first_name='J', last_name='Average')
        self.assertEqual(str(student), 'J Average')
