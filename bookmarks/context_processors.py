from bookmarks import utils
from bookmarks.models import Toast
from django.conf import settings
from django.templatetags.static import static


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
    # Handle custom logo (URL or static file path)
    custom_logo = settings.LD_CUSTOM_LOGO
    if custom_logo:
        if custom_logo.startswith(('http://', 'https://')):
            logo_url = custom_logo  # Use URL directly
        else:
            logo_url = static(custom_logo)  # Use as static file path
    else:
        logo_url = static('logo.png')  # Default logo

    return {
        "custom_name": settings.LD_CUSTOM_NAME,
        "custom_logo": logo_url,
        "show_shared_by_username": settings.LD_SHOW_SHARED_BY_USERNAME,
        "show_login_button": settings.LD_SHOW_LOGIN_BUTTON,
        "show_shared_user_filter": settings.LD_SHOW_SHARED_USER_FILTER,
    }
