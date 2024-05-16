import reflex as rx
from PythonWeb.components.navbar import navbar
from PythonWeb.views.header.header import header
from PythonWeb.views.links.links import links
from PythonWeb.components.footer import footer
class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
        rx.vstack(
        header(),
        links(),
        align="center",
        max_width="600px",)
        ),
        footer()
    )
app = rx.App()
app.add_page(index)
app._compile()
