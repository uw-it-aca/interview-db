# Copyright 2021 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from django.contrib.admin.apps import AdminConfig

class SAMLAdminConfig(AdminConfig):
    default_site = 'interview_db.admin.SAMLAdminSite'