import reflex as rx
from PythonWeb.styles.styles import *
from PythonWeb.components.link_icon import link_icon
from PythonWeb.components.info_text import info_text
from PythonWeb.styles.colors import Colors as Color
from PythonWeb.styles.colors import Fonts as Fonts

def header () -> rx.Component:
    return rx.vstack(
        rx.hstack(
        rx.avatar(name="Víctor Jiménez",
                  fallback='VJ',
                  color_scheme="yellow",
                  variant="solid",
                  high_contrast=False,
                  radius="full",
                  size="5"),
        rx.vstack(
        rx.heading("Víctor Jiménez",
                   font_size=Size.MLARGE.value,
                   margin_bottom="-15px",
                   margin_top="5px",
                   color=Color.DARKORANGE.value),
        rx.text("Desarrollador Junior, Pythonista 🐍 y Linuxero 🐧",
                font_size=Size.MEDIUM.value,
                color=Color.DARKORANGE.value),
            rx.hstack(
                link_icon("http://www.google.com"),
                link_icon("http://www.google.com"),
                link_icon("http://www.google.com"),
                link_icon("http://www.google.com"),
                margin_top="0px",
                color=Color.DARKORANGE.value,
            ),
        ),
        spacing = '5'
        ),
        rx.flex(
            info_text("Zafra, Badajoz", "España"),
        ),
        rx.text("""
Hola 👋, soy un desarrollador junior entusiasta 😊 con un sólido conocimiento en Python 🐍, HTML 🌐, C 🖥️, electrónica 🔌 y servidores 💾. 
He programado para proyectos de domótica 🛠️ y ahora estoy expandiendo mis horizontes hacia el desarrollo frontend 🎨.
        """,
                font_size=Size.LARGE.value,
                color=TextColor.WHITE.value),
        align_items="start",
        spacing='5',
        font_family=Fonts.JETBRAINS_MONO.value,
    )