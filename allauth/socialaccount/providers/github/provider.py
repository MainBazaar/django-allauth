from django.utils.encoding import python_2_unicode_compatible

from allauth.socialaccount import providers
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


@python_2_unicode_compatible
class GitHubAccount(ProviderAccount):
    def get_profile_url(self):
        return self.account.extra_data.get('html_url')

    def get_avatar_url(self):
        return self.account.extra_data.get('avatar_url')

    def __str__(self):
        dflt = super(GitHubAccount, self).__str__()
        return self.account.extra_data.get('name', dflt)


class GitHubProvider(OAuth2Provider):
    id = 'github'
    name = 'GitHub'
    package = 'allauth.socialaccount.providers.github'
    account_class = GitHubAccount

providers.registry.register(GitHubProvider)
