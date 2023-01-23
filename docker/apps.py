# Copyright 2023 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0


from django.contrib.admin.apps import AdminConfig

class InterviewAdminConfig(AdminConfig):
    default_site = 'interview_db.admin.SAMLAdminSite'
