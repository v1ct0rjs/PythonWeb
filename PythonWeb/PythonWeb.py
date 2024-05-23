import reflex as rx
from PythonWeb.components.navbar import navbar
from PythonWeb.views.header.header import header
from PythonWeb.views.links.links import links
from PythonWeb.components.footer import footer
from PythonWeb.styles.styles import *
from PythonWeb.constants import *
from PythonWeb.components.info_button import info_button

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links('Mis Proyectos', proyectos),
                links('Redes Sociales', enlaces),
                info_button('Certificaciónes', certificados),
                align="center",
                max_width=MAX_WIDTH,
                spacing='6',
                ),
            widht="100%",
            margin_y=Size.XLARGE,
        ),
        footer()
    )


app = rx.App(
    style=BASE_STYLE,
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,100..800;1,100..800&display=swap",
        "https://fonts.googleapis.com/css2?family=Major+Mono+Display&display=swap",
        "https://fonts.googleapis.com/css2?family=Major+Mono+Display&family=Ubuntu+Sans+Mono:ital,wght@0,400..700;1,400..700&display=swap"
        ],
)
app.add_page(index)
app._compile()
