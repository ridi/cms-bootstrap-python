
from django.conf import settings
from django.shortcuts import redirect

from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

from ridi.cms.login_session import COOKIE_CMS_TOKEN, COOKIE_ADMIN_ID
from ridi.cms.thrift.Errors.ttypes import NoTokenException, MalformedTokenException, ExpiredTokenException, UnauthorizedException, TException

from ${PROJECT_PATH}.cms  import admin_auth

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Read only method, or owners with write permission.
    """
    def has_permission(self, request, view):
        if settings.DEBUG and settings.CMS_AUTH_DISABLE:
            return True # Bypass at Debugging

        if request.method in permissions.SAFE_METHODS:
            return True # Allow readonly access

        token = request.COOKIES.get(COOKIE_CMS_TOKEN, None)
        try:
            required_tags = self.__get_required_tags(view)
            token = request.COOKIES.get(COOKIE_CMS_TOKEN, None)
            admin_auth.authorizeByTag(token, required_tags)
        except (NoTokenException, MalformedTokenException, ExpiredTokenException, UnauthorizedException) as e:
            raise e
        except (TException) as e:
            return False

        return True

    def __get_required_tags(self, view, tags=[]):
        if hasattr(view, 'required_tags'):
            tags = views.required_tags
        return tags