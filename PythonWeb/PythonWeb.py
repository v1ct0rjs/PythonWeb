import reflex as rx
from PythonWeb.components.navbar import navbar
from PythonWeb.views.header.header import header
from PythonWeb.views.links.links import links
from PythonWeb.components.footer import footer
from PythonWeb.styles.styles import *
from PythonWeb.constants import *

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
    style=BASE_STYLE
)
app.add_page(index)
app._compile()
