# Copyright 2025 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0


from django.test import TestCase
from interview_db.models import *
import json


class ModelsTest(TestCase):
    def setUp(self):
        self.cse = Major.objects.create(
                full_title="Computer Science Engineering",
                major_abbreviation="CSE",
            )

        self.comm = Major.objects.create(
            full_title="Communications",
            major_abbreviation="COMM",
        )

        self.hcde = Major.objects.create(
            full_title="Human Centered Design and Engineering",
            major_abbreviation="HCDE",
        )

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

        self.interview.major.set([self.cse, self.hcde, self.comm])

        self.story = Story.objects.create(
                interview=self.interview,
                story="This is Joe's first story about Learning!",
                story_order_position=1,
            )

        self.subcode = SubCode.objects.create(subcode="Context")
        self.code = Code.objects.create(
            topic="Goals (learning)",
            code="Lifelong Learning")
        self.coding = Coding(
                code=self.code,
                subcode=self.subcode,
                story=self.story,
            )

    def tearDown(self):
        Interview.objects.all().delete()
        Student.objects.all().delete()
        Major.objects.all().delete()

    def test_major_str(self):
        self.assertEqual(str(self.comm), 'COMM')
        self.assertEqual(str(self.hcde), 'HCDE')
        self.assertEqual(str(self.cse), 'CSE')

    def test_declared_major(self):
        self.assertEqual(self.interview.declared_major(), 'Communications, '
                         'Computer Science Engineering, '
                         'Human Centered Design and Engineering')

    def test_major_list(self):
        url = reverse("interview_db:major-list")
        response = self.client.get(url, follow=True)
        majors = json.loads(response.content)
        self.assertEqual(len(majors), 3)
        self.assertEqual('Communications', majors[0]['full_title'])
        self.assertEqual('Computer Science Engineering',
                         majors[1]['full_title'])
        self.assertEqual('Human Centered Design and Engineering',
                         majors[2]['full_title'])

    def test_student_str(self):
        self.assertEqual(str(self.student), 'Joe Average')

    def test_interview_str(self):
        self.assertEqual(str(self.interview), 'Joe Average: 2021-09-29')

    def test_subcode_str(self):
        self.assertEqual(str(self.subcode), 'Context')

    def test_code_str(self):
        self.assertEqual(str(self.code),
                         'Goals (learning) - Lifelong Learning')

    def test_story_str(self):
        self.assertEqual(str(self.story), 'Joe Average: 2021-09-29: 1')

    def test_short_story(self):
        self.assertEqual(self.story.short_story,
                         "This is Joe's first story about Learning!")

    def test_coding_str(self):
        self.assertEqual(str(self.coding),
                         'Goals (learning) - Lifelong Learning > Context')

    def test_collections_str(self):
        col = Collection.objects.create(
            topic='Majors',
            question='How did you choose your major?')
        self.assertEqual(str(col), 'Majors')

    def tearDown(self):
        pass
