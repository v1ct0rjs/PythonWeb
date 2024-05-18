import reflex as rx
from PythonWeb.styles.styles import *


def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        stiles=head_stile,
    )