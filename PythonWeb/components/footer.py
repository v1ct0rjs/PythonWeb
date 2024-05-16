import reflex as rx
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white", width="500px"),
        rx.link(f"link {datetime.date.today().year}", href="https://www.python.org/", is_external=True),
        rx.text("Python", font_size="20px", color="black"),
        align="center"
    )