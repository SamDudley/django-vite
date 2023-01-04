import json
import logging
from typing import Any

from django import template
from django.conf import settings
from django.templatetags.static import static
from django.utils.safestring import mark_safe

logger = logging.getLogger(__name__)

register = template.Library()

# Vite settings
VITE_DEV = getattr(settings, "VITE_DEV", False)
VITE_DEV_SERVER_URL = getattr(settings, "VITE_DEV_SERVER_URL", "http://localhost:5173")
VITE_MANIFEST_PATH = settings.VITE_MANIFEST_PATH


def load_manifest() -> dict[str, dict[str, Any]]:
    if VITE_DEV:
        return {}

    with VITE_MANIFEST_PATH.open() as f:
        manifest = json.load(f)

    logger.debug("Vite manifest loaded")

    return manifest


manifest = load_manifest()


@register.simple_tag
def vite_css(filename: str) -> str:
    if VITE_DEV:
        return ""

    return mark_safe(
        f'<link rel="stylesheet" href="{static(manifest[filename]["file"])}">'
    )


@register.simple_tag
def vite_dev_client() -> str:
    if not VITE_DEV:
        return ""

    return mark_safe(f'<script type="module" src="{VITE_DEV_SERVER_URL}/@vite/client"></script>')


@register.simple_tag
def vite_js(filename: str) -> str:
    if VITE_DEV:
        return mark_safe(f'<script type="module" src="{VITE_DEV_SERVER_URL}/{filename}"></script>')

    return mark_safe(f'<script type="module" src="{static(manifest[filename]["file"])}"></script>')
