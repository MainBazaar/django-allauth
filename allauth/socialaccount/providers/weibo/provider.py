from django.utils.encoding import python_2_unicode_compatible

from allauth.socialaccount import providers
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider

@python_2_unicode_compatible
class WeiboAccount(ProviderAccount):
    def get_profile_url(self):
        # profile_url = "u/3195025850"
        return 'http://www.weibo.com/' + self.account.extra_data.get('profile_url') 

    def get_avatar_url(self):
        return self.account.extra_data.get('avatar_large')

    def __str__(self):
        dflt = super(WeiboAccount, self).__str__()
        return self.account.extra_data.get('name', dflt)


class WeiboProvider(OAuth2Provider):
    id = 'weibo'
    name = 'Weibo'
    package = 'allauth.socialaccount.providers.weibo'
    account_class = WeiboAccount

providers.registry.register(WeiboProvider)
