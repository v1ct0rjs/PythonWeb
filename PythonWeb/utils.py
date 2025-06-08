import reflex as rx
from PythonWeb.constants import *


def lang() -> rx.Component:
    return rx.script(
        "document.documentElement.lang = 'es'; document.cookie = 'backend-enabled=false'"
    )

def lang_en() -> rx.Component:
    """Set the document language to English."""
    return rx.script(
        "document.documentElement.lang = 'en'; document.cookie = 'backend-enabled=false'"
    )

# Common
preview = "/preview.png"
avatar = "/avatar.png"
_meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:image", "content": str(preview)},
    {"name": "twitter:card", "content": "summary_large_image"},
    {"name": "twitter:site", "content": "@vmjimsan"},
]

# Información del Idex
index_title = "V1cT0r's Portfolio"
index_description = TEXTO_HEADER
index_meta = [
    {"name": "og:title", "content": str(index_title)},
    {"name": "og:description", "content": str(index_description)},
]
index_meta.extend(_meta)

# English version
eng_title = "V1cT0r's Portfolio"
eng_description = TEXT_ENG_HEADER
eng_meta = [
    {"name": "og:title", "content": str(eng_title)},
    {"name": "og:description", "content": str(eng_description)},
]
eng_meta.extend(_meta)
