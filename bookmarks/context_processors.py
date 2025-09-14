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
    def resolve_static(path, fallback):
        if path:
            if path.startswith(('http://', 'https://')):
                return path  # Use URL directly
            else:
                return static(path)  # Use as static file path
        else:
            return static(fallback)  # Default logo

    return {
        "custom_name": settings.LD_CUSTOM_NAME,
        "custom_logo": resolve_static(settings.LD_CUSTOM_LOGO, "logo.png"),
        "og_description": settings.LD_OG_DESCRIPTION,
        "og_image": resolve_static(settings.LD_OG_IMAGE, ""),
        "theme_color_light": settings.LD_THEME_COLOR_LIGHT,
        "theme_color_dark": settings.LD_THEME_COLOR_DARK,
        "show_shared_by_username": settings.LD_SHOW_SHARED_BY_USERNAME,
        "show_login_button": settings.LD_SHOW_LOGIN_BUTTON,
        "show_shared_user_filter": settings.LD_SHOW_SHARED_USER_FILTER,
    }
