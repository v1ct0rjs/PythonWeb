import reflex as rx
from PythonWeb.components.navbar import navbar
from PythonWeb.views.header.header import header
from PythonWeb.views.links.links import links
from PythonWeb.components.footer import footer
import PythonWeb.styles.styles as styles
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
        max_width=styles.MAX_WIDTH,),
        widht="100%",
        margin_y=styles.Spacer.XLARGE,
        ),
        footer()
    )
app = rx.App(
    style=styles.BASE_STYLE
)
app.add_page(index)
app._compile()
