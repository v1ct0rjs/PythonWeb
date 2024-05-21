import reflex as rx
from PythonWeb.styles.styles import *
from PythonWeb.styles.colors import Fonts


def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        stiles=head_stile,
        color=TextColor.PRIMARY.value,
        font_size=Size.XLARGE.value,
        font_family=Fonts.JETBRAINS_MONO.value,
        font_weight="700",
    )