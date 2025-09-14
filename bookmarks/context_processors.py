from bookmarks import utils
from bookmarks.models import Toast
from django.conf import settings


def toasts(request):
    user = request.user
    toast_messages = (
        Toast.objects.filter(owner=user, acknowledged=False)
        if user.is_authenticated
        else []
    )
    has_toasts = len(toast_messages) > 0

    return {
        "has_toasts": has_toasts,
        "toast_messages": toast_messages,
    }


def app_version(request):
    return {"app_version": utils.app_version}


def branding_settings(request):
    return {
        "custom_name": settings.LD_CUSTOM_NAME,
        "show_shared_by_username": settings.LD_SHOW_SHARED_BY_USERNAME,
    }
