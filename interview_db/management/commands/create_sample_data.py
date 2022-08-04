# Copyright 2022 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

# -*- coding: utf-8 -*-
"""     This provides a management command to django's manage.py called
    create_sample_spots that will generate a set of spots for testing.
"""
from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from interview_db.models import *
from django.contrib.auth.models import User
from django.core.files import File
from django.utils import timezone
from decimal import *

# from datetime import datetime
import os
import glob


class Command(BaseCommand):
    help = "Creates new data for testing"

    def handle(self, *args, **options):
        StudentType.objects.all().delete()
        Major.objects.all().delete()
        Code.objects.all().delete()
        Story.objects.all().delete()
        Interview.objects.all().delete()
        Student.objects.all().delete()
        Coding.objects.all().delete()

        cse = Major.objects.create(
            full_title="Computer Science Engineering",
            major_abbreviation="CSE",
        )
        comm = Major.objects.create(
            full_title="Communications",
            major_abbreviation="COMM",
        )
        hcde = Major.objects.create(
            full_title="Human Centered Design and Engineering",
            major_abbreviation="HCDE",
        )

        joe = Student.objects.create(
            first_name="Joe",
            last_name="Average",
            uw_netid="javerage",
            email="javerage@uw.edu",
            artifacts_url="url.com",
            follow_up_consent=False,
        )
        nancy = Student.objects.create(
            first_name="Nancy",
            last_name="Huang",
            uw_netid="nhuang1",
            email="nhuang1@uw.edu",
            artifacts_url="url.com",
            follow_up_consent=False,
        )
        billy = Student.objects.create(
            first_name="Billy",
            last_name="Joe",
            uw_netid="billyjoe",
            email="billyjoe@uw.edu",
            artifacts_url="url.com",
            follow_up_consent=False,
        )
        sam = Student.objects.create(
            first_name="Sample",
            last_name="Student",
            uw_netid="samstu",
            email="samstu@uw.edu",
            artifacts_url="url.com",
            follow_up_consent=False,
        )

        commuter = StudentType.objects.get_or_create(type="Commuter")[0]
        exchange = StudentType.objects.get_or_create(type="Exchange")[0]
        first_gen = StudentType.objects.get_or_create(type="First-Gen")[0]
        international = StudentType.objects.get_or_create(type="International")[0]

        learning = Code.objects.create(
            topic="Learning",
            code="Getting Help (learning)",
            definition="Getting Help (learning)",
        )
        career = Code.objects.create(
            topic="Career",
            code="Choosing College",
            definition="Choosing College"
        )
        identity = Code.objects.create(
            topic="Identity",
            code="Building Identity",
            definition="Building Identity",
        )
        subcode = SubCode.objects.create(
            subcode="Advice",
            definition="Advice",
        )

        i_joe = Interview.objects.create(
            student=joe,
            date="2021-09-29",
            interview_quarter="au",
            signed_release_form=True,
            pull_quote="Joe's quote about really liking UW.",
            interview_notes_url="notes.com",
            image_is_not_identifying=True,
            image_alt_text="Joe's picture",
            intended_major=True,
            standing="Freshman",
            years_until_graduation="4",
            current_year="1",
            no_identifying_photo=True,
            no_real_name=False,
            no_publishing_stories=False,
            other_publishing_restrictions=False,
        )

        i_joe.student_type.set([commuter])
        i_joe.major.set([cse])

        s_joe = Story.objects.create(
            interview=i_joe,
            story="This is Joe's first story about Getting Help (learning)",
            story_order_position=1,
        )
        s_joe.code.add(1)
        s_joe.subcode_id.add(2)

        # c_joe = Coding.objects.create(
        #     code=learning,
        #     story=s_joe
        # )
        # s_joe.subcode.add([subcode])


