from django.conf import settings

from uw_saml.utils import is_member_of_group

class SAMLGroupExecute:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if (hasattr(settings, "SAML_GROUP_EXECUTE_MAPPING")):
            for groups in settings.SAML_GROUP_EXECUTE_MAPPING:
                if all(is_member_of_group(request, group) for group in groups):
                    settings.SAML_GROUP_EXECUTE_MAPPING[groups]["="](request)
                else:
                    settings.SAML_GROUP_EXECUTE_MAPPING[groups]["!="](request)

        return self.get_response(request)