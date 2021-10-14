from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.utils import user_field, user_username, user_email, valid_email_or_none

class MyCustomAdapter(DefaultSocialAccountAdapter):

    def populate_user(self, request, sociallogin, data):
        print(sociallogin.account.provider)
        if sociallogin.account.provider == 'twitter':
            return super().populate_user(request, sociallogin, data)
        user = super().populate_user(request, sociallogin, data)
        user_username(user, data.get("username") or "")
        user_email(user, valid_email_or_none(data.get("email")) or "")
        name_parts = (data.get("name") or "").partition(" ")
        user_field(user, "primeiro_nome", data.get("first_name") or name_parts[0])
        user_field(user, "ultimo_nome", data.get("last_name") or name_parts[2])
        return user