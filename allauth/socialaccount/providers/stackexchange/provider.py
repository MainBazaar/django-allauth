from django.utils.encoding import python_2_unicode_compatible

from allauth.socialaccount import providers
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider

@python_2_unicode_compatible
class StackExchangeAccount(ProviderAccount):
    def get_profile_url(self):
        return self.account.extra_data.get('html_url')

    def get_avatar_url(self):
        return self.account.extra_data.get('avatar_url')

    def __str__(self):
        dflt = super(StackExchangeAccount, self).__str__()
        return self.account.extra_data.get('name', dflt)


class StackExchangeProvider(OAuth2Provider):
    id = 'stackexchange'
    name = 'Stack Exchange'
    package = 'allauth.socialaccount.providers.stackexchange'
    account_class = StackExchangeAccount

    def get_site(self):
        settings = self.get_settings()
        return settings.get('SITE', 'stackoverflow')

providers.registry.register(StackExchangeProvider)
