# Copyright 2024 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0


""" Management command to django's manage.py called
    create_sample_interviews that will generate interviews for testing.
"""
from django.core.management.base import BaseCommand, CommandError
from interview_db.models import *
from decimal import *


class Command(BaseCommand):
    help = "Deletes all interviews and creates new interviews for testing"

    def handle(self, *args, **options):
        print(
            "This will delete all of your existing interviews - "
            "type 'delete my interviews' to confirm:"
        )
        confirmation = input("Type it please: ")

        if confirmation != "delete my interviews":
            raise CommandError(
                "I'm only going to run if you're sure "
                "you want to 'delete my interviews'"
            )
        else:
            StudentType.objects.all().delete()
            Major.objects.all().delete()
            Coding.objects.all().delete()
            Story.objects.all().delete()
            Interview.objects.all().delete()
            Student.objects.all().delete()

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
            jane = Student.objects.create(
                first_name="Jane",
                last_name="Doe",
                uw_netid="janedoe",
                email="janedoe@uw.edu",
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

            # commuter = StudentType.objects.get_or_create(type="Commuter")[0]
            # exchange = StudentType.objects.get_or_create(type="Exchange")[0]
            # international = StudentType.objects.get_or_create(
            #     type="International")[0]

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
                standing="Fr",
                years_until_graduation="4",
                current_year="1",
                no_identifying_photo=True,
                no_real_name=False,
                no_publishing_stories=False,
                other_publishing_restrictions=False,
            )

            # i_joe.student_type.set([commuter, first_gen])
            i_joe.major.set([cse])

            s_joe = Story.objects.create(
                interview=i_joe,
                story="This is Joe's first story about Learning!",
                story_order_position=1,
            )
            s2_joe = Story.objects.create(
                interview=i_joe,
                story="This is Joe's second story about "
                      "Building Identity ... Lorem ipsum dolor sit "
                      "amet, consectetur adipiscing elit, sed do eiusmod "
                      "tempor incididunt ut labore et dolore magna aliqua."
                      " Ut enim ad minim veniam, quis nostrud exercitation "
                      "ullamco laboris nisi ut aliquip ex ea commodo "
                      "consequat. Duis aute irure dolor in reprehenderit "
                      "in voluptate velit esse cillum dolore eu fugiat "
                      "nulla pariatur. Excepteur sint occaecat cupidatat "
                      "non proident, sunt in culpa qui officia deserunt "
                      "mollit anim id est laborum.",
                story_order_position=2,
            )

            c_joe = Coding(
                code=Code.objects.get_or_create(code="Lifelong Learning")[0],
                story=s_joe,
            )
            c_joe.subcode = SubCode.objects.get_or_create(subcode="Context")[0]
            c_joe.save()

            c2_joe = Coding(
                code=Code.objects.get_or_create(code="Building Identity")[0],
                story=s2_joe,
            )
            c2_joe.subcode = SubCode.objects.get_or_create(
                subcode="Context")[0]
            c2_joe.save()

            i_jane = Interview.objects.create(
                student=jane,
                date="2022-08-04",
                interview_quarter="su",
                signed_release_form=True,
                pull_quote="Jane's really long pull quote about going to "
                           "school at UW that is very lengthy. In fact, the "
                           "quote reaches the maximum number of "
                           "characters for this field, which is a "
                           "total of two hundred characters.",
                interview_notes_url="notes.com",
                image_is_not_identifying=True,
                image_alt_text="profile",
                intended_major=False,
                standing="Jr",
                years_until_graduation="2",
                current_year="3",
                no_identifying_photo=True,
                no_real_name=False,
                no_publishing_stories=False,
                other_publishing_restrictions=False,
            )
            i_jane.major.set([cse])

            s_jane = Story.objects.create(
                interview=i_jane,
                story="This is Jane's first story about "
                      "Coming to College: Choosing College. "
                      "Lorem ipsum dolor sit amet, consectetur "
                      "adipiscing elit, sed do eiusmod tempor incididunt "
                      "ut labore et dolore magna aliqua. Ut enim ad "
                      "minim veniam, quis nostrud exercitation ullamco "
                      "laboris nisi ut aliquip ex ea commodo consequat.",
                story_order_position=1,
            )

            c_jane = Coding(
                code=Code.objects.get_or_create(code="Choosing College")[0],
                story=s_jane,
            )
            c_jane.subcode = SubCode.objects.get_or_create(
                subcode="Context")[0]
            c_jane.save()

            i_billy = Interview.objects.create(
                image="../../interview_db_vue/css/blossom.png",
                student=billy,
                date="2022-06-04",
                interview_quarter="sp",
                signed_release_form=True,
                pull_quote="Billy loves going to UW!",
                interview_notes_url="notes.com",
                image_is_not_identifying=True,
                image_alt_text="profile",
                intended_major=False,
                standing="Jr",
                years_until_graduation="3",
                current_year="2",
                no_identifying_photo=True,
                no_real_name=False,
                no_publishing_stories=False,
                other_publishing_restrictions=False,
            )
            i_billy.major.set([hcde, comm])
            # i_billy.student_type.set([exchange])

            s_billy = Story.objects.create(
                interview=i_billy,
                story="This is Billy's first story about Moving "
                      "Forward: Prove Myself. "
                      "Duis aute irure dolor in reprehenderit in "
                      "voluptate velit esse cillum dolore eu fugiat "
                      "nulla pariatur. Excepteur sint occaecat cupidatat "
                      "non proident, sunt in culpa qui officia deserunt "
                      "mollit anim id est laborum.",
                story_order_position=1,
            )
            c_billy = Coding(
                code=Code.objects.get_or_create
                (code="Prove Myself")[0],
                story=s_billy,
            )
            c_billy.subcode = SubCode.objects.get_or_create(
                subcode="Context")[0]
            c_billy.save()

            i_sam = Interview.objects.create(
                student=sam,
                date="2022-01-01",
                interview_quarter="wi",
                signed_release_form=True,
                pull_quote="I can't wait to graduate!",
                interview_notes_url="notes.com",
                image_is_not_identifying=True,
                image_alt_text="profile",
                intended_major=False,
                standing="Sr",
                years_until_graduation="< 1",
                current_year="4",
                no_identifying_photo=True,
                no_real_name=True,
                no_publishing_stories=False,
                other_publishing_restrictions=False,
            )
            i_sam.major.set([comm, cse])
            # i_sam.student_type.set([commuter, international])
            s_sam = Story.objects.create(
                interview=i_sam,
                story="This is Sam's first story about Finding Community",
                story_order_position=1,
            )
            c_sam = Coding(
                code=Code.objects.get_or_create(code="Finding Community")[0],
                story=s_sam,
            )
            c_sam.subcode = SubCode.objects.get_or_create(subcode="Context")[0]
            c_sam.save()
