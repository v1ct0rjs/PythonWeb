import reflex as rx
import datetime
from PythonWeb.styles.styles import *
from PythonWeb.styles.colors import Colors as Color

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white", width="250px"),
        rx.link(f"link {datetime.date.today().year}", href="https://www.python.org/", is_external=True, font_size=Size.MEDIUM.value),
        rx.text("Python", font_size=Size.MEDIUM.value, margin_top='-15px'),
        align="center",
        margin_bottom=Size.XLARGE.value,
        color=TextColor.GREY.value,
        background_color=Color.BACKGROUND.value,
    )