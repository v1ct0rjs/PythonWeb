import reflex as rx
from PythonWeb.styles.styles import *

def link_icon(url: str) -> rx.Component:
    return rx.link(
        rx.icon(
            tag="link", size=15
        ),
        href=url,
        is_external=True,
    )