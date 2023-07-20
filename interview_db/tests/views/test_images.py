# Copyright 2023 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.test import TestCase
from django.urls import reverse
from interview_db.models import *
from django.core.files.uploadedfile import SimpleUploadedFile
from os.path import abspath, dirname
from PIL import Image
from io import BytesIO

TEST_ROOT = abspath(dirname(__file__))


class ImagesTest(TestCase):
    def setUp(self):
        joe = Student.objects.create(
            first_name="Joe",
            follow_up_consent=False,
        )
        interview = Interview.objects.create(
            student=joe,
            date="2021-09-29",
            signed_release_form=False,
            image_is_not_identifying=True,
            intended_major=True,
            no_identifying_photo=True,
            no_real_name=False,
            no_publishing_stories=False,
            pull_quote="Some pull quote",
            other_publishing_restrictions=False
        )
        interview.image = SimpleUploadedFile(
            name='test_image.png',
            content=open("%s/../resources/test_image.png" % TEST_ROOT, 'rb').
            read(),
            content_type='image/png')
        interview.save()
        self.interview = interview

    def test_get_image(self):
        url = reverse("interview_db:student-image", kwargs={
            "id": self.interview.id})
        response = self.client.get(url, follow=True)
        image = Image.open(BytesIO(response.content))

        orig = Image.open("%s/../resources/test_image.png" % TEST_ROOT)
        self.assertEquals(image.size[0], orig.size[0])
        self.assertEquals(image.size[1], orig.size[1])
        self.assertEquals(image.format, "PNG")

    def test_no_identifying_photo(self):
        self.interview.no_identifying_photo = True
        self.interview.image_is_not_identifying = False
        self.interview.save()

        url = reverse("interview_db:student-image", kwargs={
            "id": self.interview.id})
        response = self.client.get(url, follow=True)
        self.assertEquals(response.status_code, 400)

    def test_no_image(self):
        self.interview.image.delete()
        self.interview.save()

        url = reverse("interview_db:student-image", kwargs={
            "id": self.interview.id})
        response = self.client.get(url, follow=True)
        self.assertEquals(response.status_code, 400)
