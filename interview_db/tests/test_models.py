# Copyright 2023 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0


from django.test import TestCase
from interview_db.models import *


class ModelsTest(TestCase):
    def test_major_str(self):
        major = Major.objects.create(full_title='Communications',
                                     major_abbreviation='COM')
        self.assertEqual(str(major), 'COM')

    def test_student_str(self):
        student = Student(first_name='J', last_name='Average')
        self.assertEqual(str(student), 'J Average')

    def test_collections_str(self):
        col = Collection.objects.create(
            topic='Majors',
            question='How did you choose your major?')
        self.assertEqual(str(col), 'Majors')
