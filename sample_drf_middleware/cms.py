import os
from ridi.cms.cms_client import AdminUser, AdminAuth, AdminMenu
from ridi.cms.config import Config as CmsConfig

from django.conf import settings

config = CmsConfig()

if settings.DEBUG:
    config.RPC_URL = settings.CMS_RPC_URL
else:
    import ssl

    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        # Legacy Python that doesn't verify HTTPS certificates by default
        pass
    else:
        # Handle target environment that doesn't support HTTPS verification
        ssl._create_default_https_context = _create_unverified_https_context

    config.RPC_URL = 'https://YOUR_CMS_RPC_HTTPS_DOMAIN'

admin_user = AdminUser(config)
admin_auth = AdminAuth(config)
admin_menu = AdminMenu(config)
