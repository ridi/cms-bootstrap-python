import json
import logging

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.backends import ModelBackend
from django.shortcuts import redirect

from rest_framework import authentication
from rest_framework import exceptions

from ridi.cms.login_session import COOKIE_CMS_TOKEN, COOKIE_ADMIN_ID
from ridi.cms.thrift.Errors.ttypes import *

from ${PROJECT_PATH}.cms import admin_user, admin_auth

User = get_user_model()
logger = logging.getLogger(__name__)

class CmsOpenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        username = self.__get_username(request)
        if not username:
            return None

        try:
            user = User.objects.get(id=username)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)

    def __get_username(self, request):
        if settings.DEBUG and settings.CMS_TEST_ID:
            username = settings.CMS_TEST_ID
            logger.debug('you have been permitted as ' + username)
            return username

        return request.COOKIES.get(COOKIE_ADMIN_ID, None)