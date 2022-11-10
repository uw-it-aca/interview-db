""" Management command to django's manage.py called
    create_sample_data that will generate interviews for testing.
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
            Code.objects.all().delete()
            Story.objects.all().delete()
            Interview.objects.all().delete()
            Student.objects.all().delete()
            Collection.objects.all().delete()

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

            commuter = StudentType.objects.get_or_create(type="Commuter")[0]
            exchange = StudentType.objects.get_or_create(type="Exchange")[0]
            first_gen = StudentType.objects.get_or_create(type="First-Gen")[0]
            international = StudentType.objects.get_or_create(
                type="International")[0]

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

            help = Collection.objects.create(
                topic="Getting Help",
                question="What resources have you used to help "
                         "throughout your college career?"
            )
            help.codes.set([learning])
            college = Collection.objects.create(
                topic="Coming to College",
                question="What is the biggest challenge you've "
                         "faced since coming to the UW?",
            )
            college.codes.set([career])
            reflection = Collection.objects.create(
                topic="Self Reflection",
                question="What is the biggest challenge you've "
                         "faced since coming to the UW?",
            )
            reflection.codes.set([identity])

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
            i_joe.student_type.set([commuter, first_gen])
            i_joe.major.set([cse])
            s_joe = Story.objects.create(
                interview=i_joe,
                story="This is Joe's first story about Learning, "
                      "Getting Help (learning), Advice",
                story_order_position=1,
            )
            s2_joe = Story.objects.create(
                interview=i_joe,
                story="This is Joe's second story about Identity, Building "
                      "Identity, Advice...Lorem ipsum dolor sit "
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
                code=learning,
                story=s_joe,
            )
            c_joe.subcode = subcode
            c_joe.save()
            c2_joe = Coding(
                code=identity,
                story=s2_joe,
            )
            c2_joe.subcode = subcode
            c2_joe.save()
            s_joe.code.set([learning])
            s_joe.subcode.set([subcode])
            s2_joe.code.set([identity])
            s2_joe.subcode.set([subcode])

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
                standing="Junior",
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
                story="This is Jane's first story about Career, "
                      "Choosing College, Advice "
                      "Lorem ipsum dolor sit amet, consectetur "
                      "adipiscing elit, sed do eiusmod tempor incididunt "
                      "ut labore et dolore magna aliqua. Ut enim ad "
                      "minim veniam, quis nostrud exercitation ullamco "
                      "laboris nisi ut aliquip ex ea commodo consequat.",
                story_order_position=1,
            )

            c_jane = Coding(
                code=career,
                story=s_jane,
            )
            c_jane.subcode = subcode
            c_jane.save()
            s_jane.code.set([career])
            s_jane.subcode.set([subcode])

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
                standing="Junior",
                years_until_graduation="3",
                current_year="2",
                no_identifying_photo=True,
                no_real_name=False,
                no_publishing_stories=False,
                other_publishing_restrictions=False,
            )
            i_billy.major.set([hcde])
            i_billy.student_type.set([exchange])
            s_billy = Story.objects.create(
                interview=i_billy,
                story="This is Billy's first story about Identity, "
                      "Building Identity, Advice"
                      "Duis aute irure dolor in reprehenderit in "
                      "voluptate velit esse cillum dolore eu fugiat "
                      "nulla pariatur. Excepteur sint occaecat cupidatat "
                      "non proident, sunt in culpa qui officia deserunt "
                      "mollit anim id est laborum.",
                story_order_position=1,
            )
            c_billy = Coding(
                code=identity,
                story=s_billy,
            )
            c_billy.subcode = subcode
            c_billy.save()
            s_billy.code.set([identity])
            s_billy.subcode.set([subcode])

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
                standing="Senior",
                years_until_graduation="< 1",
                current_year="4",
                no_identifying_photo=True,
                no_real_name=True,
                no_publishing_stories=False,
                other_publishing_restrictions=False,
            )
            i_sam.major.set([comm, cse])
            i_sam.student_type.set([commuter, international])
            s_sam = Story.objects.create(
                interview=i_sam,
                story="This is Sam's first story about Career, "
                      "Choosing College, Advice",
                story_order_position=1,
            )
            c_sam = Coding(
                code=identity,
                story=s_sam,
            )
            c_sam.subcode = subcode
            c_sam.save()
            s_sam.code.set([identity])
            s_sam.subcode.set([subcode])
