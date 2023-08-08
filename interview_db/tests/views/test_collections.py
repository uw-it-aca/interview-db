# Copyright 2023 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.test import TestCase
from django.urls import reverse
from interview_db.models import *
import json


class CollectionsTest(TestCase):
    fixtures = ["collections.json"]

    def test_collection_info(self):
        title = "Getting Help"
        topic = Collection.objects.get(topic=title)
        topic_id = topic.id
        question = topic.question
        slug = topic.slug

        url = reverse("interview_db:collection-info", kwargs={
            "id": topic_id})
        response = self.client.get(url, follow=True)
        info = json.loads(response.content)

        self.assertEqual(info["id"], topic_id)
        self.assertEqual(info["topic"], title)
        self.assertEqual(info["question"], question)
        self.assertEqual(info["slug"], slug)
