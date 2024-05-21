import reflex as rx
from PythonWeb.styles.styles import *


def link_icon(url: str, icon: str) -> rx.Component:
    return rx.link(
        rx.icon(
            tag=icon, size=20
        ),
        href=url,
        is_external=True,
    )