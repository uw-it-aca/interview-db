# Copyright 2023 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0


from django.test import TestCase
from interview_db.models import *


class ModelsTest(TestCase):
    def setUp(self):
        cse = Major.objects.create(
                full_title="Computer Science Engineering",
                major_abbreviation="CSE",
            )
        self.cse = cse

        comm = Major.objects.create(
            full_title="Communications",
            major_abbreviation="COMM",
        )
        self.comm = comm

        hcde = Major.objects.create(
            full_title="Human Centered Design and Engineering",
            major_abbreviation="HCDE",
        )
        self.hcde = hcde

        joe = Student.objects.create(
            first_name="Joe",
            last_name="Average",
            follow_up_consent=False,
        )
        self.student = joe

        i_joe = Interview.objects.create(
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

        i_joe.major.set([cse, hcde, comm])
        self.i_joe = i_joe

    def tearDown(self):
        Interview.objects.all().delete()
        Student.objects.all().delete()
        Major.objects.all().delete()

    def test_major_str(self):
        self.assertEqual(str(self.comm), 'COMM')
        self.assertEqual(str(self.hcde), 'HCDE')
        self.assertEqual(str(self.cse), 'CSE')

    def test_declared_major(self):
        self.assertEqual(self.i_joe.declared_major(), 'Communications, '
                         'Computer Science Engineering, '
                         'Human Centered Design and Engineering')

    def test_student_str(self):
        self.assertEqual(str(self.student), 'Joe Average')

    def test_collections_str(self):
        col = Collection.objects.create(
            topic='Majors',
            question='How did you choose your major?')
        self.assertEqual(str(col), 'Majors')
